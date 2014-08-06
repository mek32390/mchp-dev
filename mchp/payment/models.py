from django.db import models
from django.contrib.auth.models import User

class StripeCustomer(models.Model):
    user = models.ForeignKey(User, related_name='stripe')
    stripe_id = models.CharField(max_length=100)
    recipient_id = models.CharField(max_length=100)

    create_date = models.DateTimeField(auto_now_add=True)

    class Meta:
        unique_together = ('user', 'stripe_id')

    def __str__(self):
        return "{} added a cc".format(self.user.username)
