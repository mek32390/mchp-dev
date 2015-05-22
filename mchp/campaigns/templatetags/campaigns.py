from django import template
from django.core.urlresolvers import reverse
from django.utils.http import urlquote
from django.utils.safestring import mark_safe

register = template.Library()


# [TODO] should probably be in settings
BASE_DOMAIN = 'http://www.mycollegehomepage.com'


@register.filter
def track_click(value, arg):
    """ Rewrite link to track click from subscriber with next url arg.

    """
    url = reverse('campaign-click', kwargs={'uuid': value.uuid})
    return '{}{}?next={}'.format(BASE_DOMAIN, url, urlquote(arg))


@register.filter
def track_open(value):
    """ Rewrite link to track open from subscriber.

    """
    url = reverse('campaign-open', kwargs={'uuid': value.uuid})
    return mark_safe('<img src="{}{}" alt="Beacon">'.format(BASE_DOMAIN, url))


@register.filter
def track_unsubscribe(value, arg):
    """ Rewrite link to track unsubscribe from subscriber with next url arg.

    """
    url = reverse('campaign-unsubscribe', kwargs={'uuid': value.uuid})
    return '{}{}?next={}'.format(BASE_DOMAIN, url, urlquote(arg))
