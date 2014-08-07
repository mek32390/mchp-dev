from django.db import models
from django.contrib.auth.models import User

from payment import managers

from jsonfield import JSONField

class StripeCustomer(models.Model):
    user = models.ForeignKey(User, related_name='stripe')
    stripe_id = models.CharField(max_length=100)
    recipient_id = models.CharField(max_length=100, blank=True, null=True)

    default = models.BooleanField(default=False)
    last_four = models.CharField(max_length=4)

    create_date = models.DateTimeField(auto_now_add=True)

    objects = managers.StripeCustomerManager()

    class Meta:
        unique_together = ('user', 'stripe_id')

    def __str__(self):
        return "{} added a cc".format(self.user.username)

class WebhookMessage(models.Model):
    message = JSONField()
