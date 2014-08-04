from django import template
from django.template import Library
from django.conf import settings

register = Library()

@register.inclusion_tag('payment.html')
def payment_dialog(modal_id=None, student=None):
    return {
        'modal_id': modal_id,
        'student': student,
    }

@register.inclusion_tag('purchase.html')
def purchase(student=None):
    return {
        'student': student,
    }

@register.inclusion_tag('card_info.html')
def card_info(student=None):
    return {
        'student': student,
    }

@register.inclusion_tag('cash_out.html')
def cash_out(student=None):
    return {
        'student': student,
    }

class StripePublicKeyNode(template.Node):
    def render(self, context):
        return '<script type="text/javascript">' + \
          'Stripe.setPublishableKey("' + settings.STRIPE_PUBLIC_KEY + '");' + \
        '</script>'

@register.tag
def stripe_public_key(parser, token):
    return StripePublicKeyNode()
