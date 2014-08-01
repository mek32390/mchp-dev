from django.template import Library

register = Library()

@register.inclusion_tag('referral_dialog.html')
def referral_dialog(modal_id=None):
    return {'modal_id': modal_id}
