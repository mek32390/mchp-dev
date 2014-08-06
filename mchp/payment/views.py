from django.contrib import messages
from django.conf import settings
from django.core.urlresolvers import reverse
from django.shortcuts import redirect
from django.http import HttpResponse
from django.utils.decorators import method_decorator
from django.views.generic.edit import View
from django.views.decorators.csrf import csrf_exempt
from django.views.decorators.http import require_POST

from lib.decorators import school_required
from payment.models import StripeCustomer, WebhookMessage
from decimal import Decimal, ROUND_HALF_DOWN

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
            stripe.api_key = settings.STRIPE_SECRET_KEY

            # Get the credit card details submitted by the form
            token = request.POST['stripeToken']

            # Create a Customer
            customer, response = self.customer_stripe_errors(token)
            if not customer:
                return response

            # make them a recipient so they can cash out
            exp = request.POST.get('expiry', '')
            month = int(exp.split('/')[0])
            year = int(exp.split('/')[1])
            try:
                recipient = stripe.Recipient.create(
                    name=request.POST.get('name', ''),
                    type="individual",
                    email=self.student.user.email,
                    card = {
                        'number': request.POST.get('number', ''),
                        'exp_month': month,
                        'exp_year': year,
                        'cvc': request.POST.get('cvc', ''),
                        'name': request.POST.get('name', ''),
                    },
                )
            except stripe.error.StripeError as e:
                body = e.json_body
                err = body['error']
                data = {
                    'response': err['message']
                }
                return self.render_to_json_response(data, status=e.http_status)
            sc = StripeCustomer(
                user=request.user,
                stripe_id = customer.id,
                recipient_id = recipient.id,
            )
            sc.save()


            # everything worked
            messages.info(
                self.request,
                'card info saved',
            )
            data = {
                'messages': self.ajax_messages(),
            }
            return self.render_to_json_response(data)
        else:
            return redirect(reverse('my_profile'))

    def customer_stripe_errors(self, token):
        customer = []
        try: 
            customer = stripe.Customer.create(
                card=token,
                description=self.student.name()
            )
        except stripe.error.CardError as e: 
            body = e.json_body
            err = body['error']
            data ={
                'response': err['message'],
            }
            return None, self.render_to_json_response(data, status=e.http_status)
        except stripe.error.AuthenticationError as e:
            data ={
                'response': 'Authentication error',
            }
            return None, self.render_to_json_response(data, status=403)
        except stripe.error.APIConnectionError as e:
            data ={
                'response': 'Connection error',
            }
            return None, self.render_to_json_response(data, status=403)
        except stripe.error.StripeError as e:
            body = e.json_body
            err = body['error']
            data = {
                'response': err['message']
            }
            return None, self.render_to_json_response(data, status=e.http_status)
        except Exception as e:
            data ={
                'response': 'Something else happened',
            }
            return None, self.render_to_json_response(data, status=500)
        return customer, None

    @method_decorator(school_required)
    def dispatch(self, *args, **kwargs):
        self.student = self.request.user.student
        return super(SaveInfoView, self).dispatch(*args, **kwargs)

save_info = SaveInfoView.as_view()

class ChargeView(View, AjaxableResponseMixin):
    def get(self, request, *args, **kwargs):
        return redirect(reverse('my_profile'))

    def post(self, request, *args, **kwargs):
        if request.is_ajax():
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
            'balance': self.student.display_balance(),
            'points': self.student.total_points(),
        }
        return self.render_to_json_response(data)


    @method_decorator(school_required)
    def dispatch(self, *args, **kwargs):
        self.student = self.request.user.student
        return super(ChargeView, self).dispatch(*args, **kwargs)

charge = ChargeView.as_view()

class PayoutView(View, AjaxableResponseMixin):
    def get(self, request, *args, **kwargs):
        return redirect(reverse('my_profile'))

    def post(self, request, *args, **kwargs):
        if request.is_ajax():
            amount = self.student.balance 
            cents = int(amount.quantize(Decimal('1.00'), rounding=ROUND_HALF_DOWN)) * 100
            if cents < 2000:
                messages.error(
                    self.request,
                    "You can't cash out till you reach $20",
                )
                status = 402
                data = {
                    'messages': self.ajax_messages(),
                }
                return self.render_to_json_response(data, status=status)

            customer = StripeCustomer.objects.filter(
                user = request.user
            )
            if customer.exists():
                recipient_id = customer[0].recipient_id
                try:
                    stripe.api_key = settings.STRIPE_SECRET_KEY
                    stripe.Transfer.create( 
                        amount=cents, 
                        currency="usd", 
                        recipient=recipient_id,
                        description="Cash out for {}".format(self.student.user.email)
                    )
                except stripe.error.StripeError as e:
                    data = {
                        'response': e
                    }
                    return self.render_to_json_response(data, status=402)

                self.student.balance = 0.0000
                self.student.save()
                messages.success(
                    self.request,
                    "You will recieve your funds in a few days, hold tight",
                )
                status = 200
            else:
                messages.error(
                    self.request,
                    "You havn't entered a dept card yet",
                )
                status = 402
            data = {
                'messages': self.ajax_messages(),
            }
            return self.render_to_json_response(data, status=status)
        else:
            return redirect(reverse('my_profile'))

    @method_decorator(school_required)
    def dispatch(self, *args, **kwargs):
        self.student = self.request.user.student
        return super(PayoutView, self).dispatch(*args, **kwargs)

payout = PayoutView.as_view()

class WebhookView(View):

    def post(self, request, *args, **kwargs):
        print(request.body)
        event_json = json.loads(request.body.decode('utf-8'))
        hook = WebhookMessage(message = event_json)
        hook.save()
        return HttpResponse(status=200)

    @method_decorator(csrf_exempt)
    @method_decorator(require_POST)
    def dispatch(self, *args, **kwargs):
        return super(WebhookView, self).dispatch(*args, **kwargs)

webhook = WebhookView.as_view()
