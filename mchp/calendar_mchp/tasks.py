from __future__ import absolute_import
from decimal import Decimal, ROUND_HALF_DOWN

from django.utils import timezone
from django.conf import settings

from celery.decorators import task
from celery.utils.log import get_task_logger

from calendar_mchp.models import Subscription

logger = get_task_logger(__name__)

@task
def bill_collector():
    subscriptions = Subscription.objects.filter(
        payment_date__lte=timezone.now()
    )
    for subscription in subscriptions:
        student = subscription.student
        # TODO: send a notification
        if student.reduce_points(subscription.price):
            subscription.enabled = True
            subscription.payment_date = subscription.payment_date + \
                    settings.MCHP_PRICING['subscription_length']
            subscription.save()

            calendar = subscription.calendar
            points = calendar.price * (settings.MCHP_PRICING['commission_rate'] / 100)
            points = points / 100
            points = Decimal(points).quantize(Decimal('1.0000'), rounding=ROUND_HALF_DOWN)
            calendar.owner.modify_balance(points)
            calendar.owner.save()
        else:
            subscription.enabled = False
            subscription.payment_date = subscription.payment_date + \
                    settings.MCHP_PRICING['delinquent_subscription_length']
            subscription.save()
