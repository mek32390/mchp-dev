from django.db import models

class PageHit(models.Model):
    agent = models.CharField(max_length=300)
    time = models.DateTimeField('date accessed')
