from django.contrib import messages
from django.conf import settings
from django.core.urlresolvers import reverse
from django.shortcuts import redirect
from django.http import HttpResponse
from django.utils.decorators import method_decorator
from django.views.generic.edit import View

from lib.decorators import school_required
from payment.models import StripeCustomer
from decimal import Decimal

import json
import stripe

'''
url: /referral/redeem/
name: referral_redeem
'''
class AjaxableResponseMixin(object):
    """
    Mixin to add AJAX support to a form.

    I stole this right from the django website.
    """
    def render_to_json_response(self, context, **response_kwargs):
        data = json.dumps(context)
        response_kwargs['content_type'] = 'application/json'
        return HttpResponse(data, **response_kwargs)

    def ajax_messages(self):
        django_messages = []

        for message in messages.get_messages(self.request):
            django_messages.append({
                "level": message.level,
                "message": message.message,
                "extra_tags": message.tags,
            })
        return django_messages

class SaveInfoView(View, AjaxableResponseMixin):
    def get(self, request, *args, **kwargs):
        return redirect(reverse('my_profile'))

    def post(self, request, *args, **kwargs):
        if request.is_ajax():
            print(request.POST)
            stripe.api_key = settings.STRIPE_SECRET_KEY

            # Get the credit card details submitted by the form
            token = request.POST['stripeToken']

            # Create a Customer
            customer = stripe.Customer.create(
                card=token,
                description=self.student.name()
            )
            sc = StripeCustomer(
                user=request.user,
                stripe_id = customer.id,
            )
            sc.save()

            messages.info(
                self.request,
                'cc info saved',
            )
            data = {
                'messages': self.ajax_messages(),
            }
            return self.render_to_json_response(data)
        else:
            return redirect(reverse('my_profile'))

    @method_decorator(school_required)
    def dispatch(self, *args, **kwargs):
        self.student = self.request.user.student
        return super(SaveInfoView, self).dispatch(*args, **kwargs)

save_info = SaveInfoView.as_view()

class ChargeView(View, AjaxableResponseMixin):
    def get(self, request, *args, **kwargs):
        print('um')
        return redirect(reverse('my_profile'))

    def post(self, request, *args, **kwargs):
        if request.is_ajax():
            print(request.POST)
            purchase_type = json.loads(request.POST.get('type', ''))
            if purchase_type.lower() == 'card':
                return self._card_charge(request)
            elif purchase_type.lower() == 'savings':
                return self._savings_charge(request)
            else:
                return redirect(reverse('my_profile'))
        else:
            return redirect(reverse('my_profile'))

    def _card_charge(self, request):
        stripe.api_key = settings.STRIPE_SECRET_KEY

        customer = StripeCustomer.objects.filter(
            user = request.user
        )
        amount = request.POST.get('amount', 0)
        if customer.exists():
            customer_id = customer[0].stripe_id
            res = stripe.Charge.create(
                amount=amount,
                currency="usd",
                customer=customer_id
            )
            print(res)
            if res.paid and not res.failure_code:
                self.student.add_purchased_points(int(amount))
                amount = Decimal(res.amount)/100
                messages.success(
                    self.request,
                    'Your card has been charged $'+str(amount),
                )
            else:
                messages.error(
                    self.request,
                    res.failure_message
                )

        else:
            messages.error(
                self.request,
                'You have not added a card',
            )

        data = {
            'messages': self.ajax_messages(),
        }
        return self.render_to_json_response(data)

    def _savings_charge(self, request):
        amount = int(request.POST.get('amount', ''))
        decimal_amount = Decimal(amount)/100
        if self.student.balance < decimal_amount:
            messages.error(
                self.request,
                "Better hustle some more, you don't have the savings for that.",
            )
        else:
            self.student.modify_balance(-decimal_amount)
            self.student.add_purchased_points(amount)
            messages.success(
                self.request,
                "Purchase success, your balance is now $" + self.student.display_balance(),
            )
        data = {
            'messages': self.ajax_messages(),
        }
        return self.render_to_json_response(data)


    @method_decorator(school_required)
    def dispatch(self, *args, **kwargs):
        self.student = self.request.user.student
        return super(ChargeView, self).dispatch(*args, **kwargs)

charge = ChargeView.as_view()
