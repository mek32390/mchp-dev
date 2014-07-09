from django.db import models
from django.db.models.signals import post_delete
from django.dispatch.dispatcher import receiver
from django.template.defaultfilters import slugify

from documents.exceptions import DuplicateFileError

import hashlib
import uuid
import os.path

class Document(models.Model):
    title = models.CharField(max_length=200)
    description = models.TextField(blank=True)

    up = models.IntegerField(default=0)
    down = models.IntegerField(default=0)
    price = models.PositiveIntegerField(default=0)

    document = models.FileField(upload_to="documents/%Y/%m")
    md5sum = models.CharField(max_length=32)
    uuid = models.CharField(max_length=32)
    create_date = models.DateTimeField(auto_now_add=True)

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

    def filename(self):
        return os.path.basename(self.document.name)

    def rating(self):
        return self.up - self.down

    def __str__(self):
        return "{}".format(self.title)

# Receive the pre_delete signal and delete the file associated with the model instance.
@receiver(post_delete, sender=Document)
def document_delete(sender, instance, **kwargs):
    # Pass false so FileField doesn't save the model.
    if instance.document:
        instance.document.delete(False)

class Upload(models.Model):
    document = models.ForeignKey(Document)
    owner = models.ForeignKey('user_profile.student')

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
