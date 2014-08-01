from django.template import Library
from django.template.defaultfilters import stringfilter

register = Library()

@register.inclusion_tag('referral_dialog.html')
def referral_dialog(modal_id=None):
    return {'modal_id': modal_id}


@register.filter
@stringfilter
def referral(value, arg):
    return value + "?ref=" + arg
