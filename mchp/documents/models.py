from django.db import models

class Document(models.Model):
    title = models.CharField(max_length=60)
    description = models.TextField(blank=True)
    rating = models.IntegerField(default=0)
    price = models.DecimalField(max_digits=5, decimal_places=2, default=0.00)
    purchased = models.IntegerField(default=0)
    document = models.FileField(upload_to="documents/%Y/%m")
    create_date = models.DateTimeField(auto_now_add=True)
    slug = models.SlugField(max_length=60)

class Upload(models.Model):
    document = models.ForeignKey(Document)
    owner = models.ForeignKey('user_profile.student')
