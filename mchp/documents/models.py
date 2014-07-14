from django.conf import settings
from django.db import models
from django.template.defaultfilters import slugify

from documents.exceptions import DuplicateFileError
from schedule.models import School, Course

import hashlib
import uuid
import os.path
import magic

import logging
logger = logging.getLogger(__name__)

DOCUMENT_LOCATION = "documents/%Y/%m"
PREVIEW_LOCATION = "previews"

def get_sentinel_course():
    school, created = School.objects.get_or_create(domain='deleted.edu', name='deleted')
    course, created = Course.objects.get_or_create(domain=school, 
                                        dept='del', 
                                        course_number=100,
                                        professor='deleted')
    return course

class Document(models.Model):
    title = models.CharField(max_length=200)
    description = models.CharField(max_length=1000)
    course = models.ForeignKey('schedule.Course', on_delete=models.SET(get_sentinel_course))

    up = models.IntegerField(default=0)
    down = models.IntegerField(default=0)
    price = models.PositiveIntegerField(default=0)

    document = models.FileField(upload_to=DOCUMENT_LOCATION)
    md5sum = models.CharField(max_length=32)
    uuid = models.CharField(max_length=32)
    create_date = models.DateTimeField(auto_now_add=True)

    preview = models.ImageField(upload_to=PREVIEW_LOCATION, blank=True, null=True)
    slug = models.SlugField(max_length=80)
    
    def save(self, *args, **kwargs):
        if not self.pk: # object is new
            hash = hashlib.md5()
            for chunk in self.document.chunks():
                hash.update(chunk)
            self.md5sum = hash.hexdigest()
            
            if Document.objects.filter(md5sum=self.md5sum).exists():
                raise DuplicateFileError("This file already has already been uploaded")

            self.slug = slugify(self.title)[:80]
            self.uuid = uuid.uuid4().hex

        super(Document, self).save(*args, **kwargs)

    # if document.name is called before its actually saved, it will be different than the name on
    # disk
    def filetype(self):
        loc = settings.MEDIA_ROOT + '/' + self.document.name
        return magic.from_file(loc, mime=True)

    def filename(self):
        return os.path.basename(self.document.name)

    def purchase_count(self):
        return DocumentPurchase.objects.filter(document=self).count()

    def review_count(self):
        return 0

    def rating(self):
        return self.up - self.down

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
        if self.normalize_positive_votes() == 0:
            return 0
        else: 
            return 100 - self.normalize_positive_votes()

    def __str__(self):
        return "{}".format(self.title)

class Upload(models.Model):
    document = models.ForeignKey(Document)
    owner = models.ForeignKey('user_profile.Student')

    class Meta:
        unique_together = ('document', 'owner')

    def __str__(self):
        return "{} uploaded {}".format(
            self.owner.user.username, 
            self.document.title)

class DocumentPurchase(models.Model):
    document = models.ForeignKey(Document, related_name='purchased_document')
    student = models.ForeignKey('user_profile.Student')

    class Meta:
        unique_together = ('document', 'student')

    def __str__(self):
        return "{} bought {}".format(
            self.student.user.username, 
            self.document.title)
