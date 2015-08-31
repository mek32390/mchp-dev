from django.db import models
from django.template.defaultfilters import slugify
from django.core.urlresolvers import reverse
from django.conf import settings
from django.utils import timezone

from documents.exceptions import DuplicateFileError
from documents.s3utils import S3Auth
from schedule.models import School, Course
from documents import managers

import hashlib
import uuid
import os.path
import magic

import logging
logger = logging.getLogger(__name__)

DOCUMENT_LOCATION = "documents/"
PREVIEW_LOCATION = "previews/"


def get_sentinel_course():
    school, created = School.objects.get_or_create(domain='deleted.edu', name='deleted')
    course, created = Course.objects.get_or_create(domain=school, 
                                        dept='del', 
                                        course_number=100,
                                        professor='deleted')
    return course


class Document(models.Model):

    STUDY_GUIDE = 0
    SYLLABUS = 1

    DOCUMENT_TYPE_CHOICES = (
        (STUDY_GUIDE, 'Study guide'),
        (SYLLABUS, 'Syllabus'),
    )

    type = models.IntegerField(default=STUDY_GUIDE, choices=DOCUMENT_TYPE_CHOICES)

    title = models.CharField(max_length=200)
    description = models.CharField(max_length=1000)
    course = models.ForeignKey('schedule.Course', on_delete=models.SET(get_sentinel_course))

    up = models.IntegerField(default=0)
    down = models.IntegerField(default=0)
    price = models.PositiveIntegerField(default=400)

    document = models.FileField(upload_to=DOCUMENT_LOCATION)
    filetype = models.CharField(max_length=150)
    md5sum = models.CharField(max_length=32)
    uuid = models.CharField(max_length=32)
    create_date = models.DateTimeField(auto_now_add=True)

    approved = models.BooleanField(default=True)
    roster_upload = models.ForeignKey('rosters.Roster', null=True)

    preview = models.ImageField(upload_to=PREVIEW_LOCATION, blank=True, null=True)
    slug = models.SlugField(max_length=80)

    objects = managers.DocumentManager()
    
    '''
    Add a bunch of information and check for duplicates before saving

    also, those seeks are absolutely fucking necessary with the s3 stuff
    '''
    def save(self, *args, **kwargs):
        if not self.pk: # object is new
            if self.document.size < 1:
                # ya, I know, maybe all empty files are duplicates of the same file 
                raise DuplicateFileError("No empty files")
            hash = hashlib.md5()
            for chunk in self.document.chunks():
                hash.update(chunk)
            self.md5sum = hash.hexdigest()
            self.document.file.seek(0,0)
            
            if Document.objects.filter(md5sum=self.md5sum).exists():
                raise DuplicateFileError("This file already has already been uploaded")

            chunk = self.document.file.read(1024)
            self.filetype = magic.from_buffer(chunk, mime=True)
            self.document.file.seek(0,0)
            self.slug = slugify(self.title)[:80]
            self.uuid = uuid.uuid4().hex

        super(Document, self).save(*args, **kwargs)

    def get_absolute_url(self):
        return reverse('document_detail', args=[str(self.uuid)])

    def filename(self):
        return os.path.basename(self.document.name)

    def purchase_count(self):
        return DocumentPurchase.objects.filter(document=self).count()

    def review_count(self):
        return DocumentPurchase.objects.filter(document=self).exclude(review_date=None).count()

    def rating(self):
        return self.up - self.down

    def tmp_url(self):
        doc = self.document
        s = S3Auth(settings.AWS_ACCESS_KEY_ID, settings.AWS_SECRET_ACCESS_KEY)
        url = s.get_v2(settings.AWS_STORAGE_BUCKET_NAME, '/media/' + doc.name)
        return url

    '''
    converts the number of postive votes to a score on a scale of 0-100

    OldRange = (OldMax - OldMin)  
    NewRange = (NewMax - NewMin)  
    NewValue = (((OldValue - OldMin) * NewRange) / OldRange) + NewMin
    '''
    def normalize_positive_votes(self):
        if self.up < 1:
            return 0
        else:
            return ((self.up * 100) / (self.up + self.down))

    # same, but for negative votes
    def normalize_negative_votes(self):
        if self.down < 1:
            return 0
        elif self.normalize_positive_votes() == 0:
            return 100
        else: 
            return 100 - self.normalize_positive_votes()

    def __str__(self):
        return "{}".format(self.title)

class Upload(models.Model):
    document = models.OneToOneField(Document)
    owner = models.ForeignKey('user_profile.Student')

    class Meta:
        unique_together = ('document', 'owner')

    def save(self, *args, **kwargs):
        from documents.signals import document_uploaded
        signal = False
        if not self.pk:
            signal = True
        super(Upload, self).save(*args, **kwargs)
        if signal:
            document_uploaded.send(sender=self.__class__, upload=self)


    def __str__(self):
        return "{} uploaded {}".format(
            self.owner.user.username, 
            self.document.title)

class DocumentPurchase(models.Model):
    document = models.ForeignKey(Document, related_name='purchased_document')
    student = models.ForeignKey('user_profile.Student')
    purchase_date = models.DateTimeField(auto_now_add=True)

    review = models.CharField(max_length=250, blank=True)
    review_date = models.DateTimeField(blank=True, null=True)

    class Meta:
        unique_together = ('document', 'student')

    def save(self, *args, **kwargs):
        from documents.signals import document_purchased
        signal = False
        if not self.pk:
            signal=True
        super(DocumentPurchase, self).save(*args, **kwargs)
        if signal:
            document_purchased.send(sender=self.__class__, purchase=self)

    def __str__(self):
        return "{} bought {}".format(
            self.student.user.username, 
            self.document.title)

'''
Document flagging
'''
# flag status
FLAGGED = 1
REVIEWED = 2
CLOSED = 3
REMOVED = 4
FLAG_CHOICES = [
    (FLAGGED, 'Flagged'),
    (REVIEWED, 'Under review'),
    (CLOSED, 'Ticket closed'),
    (REMOVED, 'Content removed'),
]

# report reasons
PROFESSOR = 1
DUPLICATE = 2
OTHER = 3
FLAG_REASONS = [
    (PROFESSOR, 'Instructor notes'),
    (DUPLICATE, 'Duplication Document'),
    (OTHER, 'Other reason'),
]

class DocumentFlag(models.Model):
    document = models.ForeignKey('Document', related_name='flags')
    
    status = models.PositiveIntegerField(choices=FLAG_CHOICES, default=FLAGGED)
    reason = models.PositiveSmallIntegerField(choices=FLAG_REASONS)
    created = models.DateTimeField(auto_now_add=True)
    closed = models.DateTimeField(blank=True, null=True)

    student = models.ForeignKey('user_profile.Student')
    ip = models.IPAddressField(blank=True, null=True)
    
    detail = models.CharField(max_length=300, blank=True)
    staff_comment = models.TextField(blank=True, null=True)

    def close(self, status=CLOSED):
        self.status = status
        self.closed = timezone.now()

    def __unicode__(self):
        return '{} has been flagged by {} ({})'.format(self.document.name, 
                                                       self.student.user.user_name,
                                                       self.ip)
