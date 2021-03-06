from django import template
from django.core.urlresolvers import reverse
from django.utils.html import smart_urlquote
from django.utils.safestring import mark_safe

register = template.Library()


@register.filter
def track_click(value, arg):
    """ Rewrite link to track click from subscriber with next URL `arg`.

    """
    url = reverse('studyguide-click', kwargs={'uuid': value.uuid})
    return smart_urlquote('{}?next={}'.format(url, arg))


@register.filter
def track_open(value):
    """ Rewrite link to track open from subscriber.

    """
    url = reverse('studyguide-open', kwargs={'uuid': value.uuid})
    img_src = '<img src="{}" alt="Beacon" height="1" width="1">'
    return mark_safe(img_src.format(url))


@register.filter
def track_unsubscribe(value):
    """ Rewrite link to track unsubscribe from subscriber with next URL `arg`.

    """
    return reverse('studyguide-unsubscribe', kwargs={'uuid': value.uuid})
