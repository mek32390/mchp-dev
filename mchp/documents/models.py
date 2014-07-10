from django.conf import settings
from django.db import models
from django.db.models.signals import post_delete, post_save
from django.dispatch.dispatcher import receiver
from django.template.defaultfilters import slugify

from documents.exceptions import DuplicateFileError
from schedule.models import School, Course

import hashlib
import uuid
import os.path
import subprocess
import magic

import logging
logger = logging.getLogger(__name__)

DOCUMENT_LOCATION = "documents/%Y/%m"
THUMBNAIL_LOCATION = "thumbnails"
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

    thumbnail = models.ImageField(upload_to=THUMBNAIL_LOCATION, blank=True, null=True)
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

    def __str__(self):
        return "{}".format(self.title)

#FIXME: woah
@receiver(post_save, sender=Document)
def create_thumbnail(sender, instance, **kwargs):
    # don't do this more than once 
    if not kwargs['created']:
        return 

    # add generated thumbnail filename
    thumbnail = THUMBNAIL_LOCATION + "/{}_thumb.png".format(
        os.path.splitext(instance.filename())[0]
    )
    instance.thumbnail = thumbnail
    # add generated preview filename
    preview = PREVIEW_LOCATION + "/{}_preview.png".format(
        os.path.splitext(instance.filename())[0]
    )
    instance.preview = preview
    instance.save()

    # first make sure dirs exist
    os.makedirs(settings.MEDIA_ROOT + '/' + THUMBNAIL_LOCATION, exist_ok=True)
    os.makedirs(settings.MEDIA_ROOT + '/' + PREVIEW_LOCATION, exist_ok=True)

    # word_types = ['application/doc', 'application/docx', 'application/text']
    if instance.filetype() != b'application/pdf':
        return

    # first make thumbnail
    command = "convert -quality 95 -thumbnail 64 -background white\
            {}/{}[0] {}/{}".format(
        settings.MEDIA_ROOT, instance.document, settings.MEDIA_ROOT, instance.thumbnail)
    convert(command)

    # now make preview
    command = "convert -quality 95 -thumbnail 500 -background white\
            {}/{}[0] {}/{}".format(
        settings.MEDIA_ROOT, instance.document, settings.MEDIA_ROOT, instance.preview)
    convert(command)

def convert(command):
    logger.debug(command)

    proc = subprocess.Popen(command,
        shell=True,
        stdin=subprocess.PIPE,
        stdout=subprocess.PIPE,
        stderr=subprocess.PIPE,
    )
    stdout_value = proc.communicate()[0]
    logger.debug('stdout: ' + str(stdout_value))

# Receive the pre_delete signal and delete the file associated with the model instance.
@receiver(post_delete, sender=Document)
def document_delete(sender, instance, **kwargs):
    # Pass false so FileField doesn't save the model.
    if instance.document:
        instance.document.delete(False)
    if instance.thumbnail:
        instance.thumbnail.delete(False)
    if instance.preview:
        instance.preview.delete(False)

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
