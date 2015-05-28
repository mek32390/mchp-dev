from django.core.mail import EmailMultiAlternatives
from django.utils import timezone
from django.utils.html import strip_tags
import uuid


def make_email_message(subject, body, sender, recipient, connection):
    """ Build an EmailMessage with HTML and plain text alternatives.

    Parameters
    ----------
    subject : str
        A subject for this message.  Limited to 78 characters.
    body : str
        A body for this message.
    sender : str
        An e-mail address (and optional name) from which to send.
    recipient : str
        An e-mail address (and optional name) to which to send.
    connection : django.core.mail.backends.console.EmailBackend
        A connection through which to send the message.

    """
    msg = EmailMultiAlternatives(subject, strip_tags(body),
                                 sender, [recipient],
                                 connection=connection)
    msg.attach_alternative(body, "text/html")
    return msg


def make_uuid():
    return uuid.uuid4().hex


def make_display_email(address, name=None):
    """ Create a display e-mail adress, such as:

        mchp <study@mycollegehomepage.com>

    """
    if name:
        name = name.replace('"', '\\"')
        return '{} <{}>'.format(name, address)
    else:
        return address


def handle_click(subscriber):
    """ Subscriber clicked through from an e-mail.

    Notes
    -----
    This is here to allow CampaignSubscriber subclasses to use this feature.

    """
    if not subscriber.clicked:
        subscriber.clicked = timezone.now()
        subscriber.save(update_fields=['clicked'])


def handle_open(subscriber):
    """ Subscriber opened an e-mail.

    Notes
    -----
    This is here to allow CampaignSubscriber subclasses to use this feature.

    Response code is 204 "no content," per <http://stackoverflow.com/questions/6638504/why-serve-1x1-pixel-gif-web-bugs-data-at-all>.  # noqa

    """
    if not subscriber.opened:
        subscriber.opened = timezone.now()
        subscriber.save(update_fields=['opened'])


def handle_unsubscribe(subscriber):
    """ Subscriber unsubscribed from an e-mail.

    Notes
    -----
    This is here to allow CampaignSubscriber subclasses to use this feature.

    """
    if not subscriber.unsubscribed:
        subscriber.unsubscribed = timezone.now()
        subscriber.save(update_fields=['unsubscribed'])


def handle_resubscribe(subscriber):
    """ Subscriber unsubscribed from an e-mail.

    Notes
    -----
    This is here to allow CampaignSubscriber subclasses to use this feature.

    """
    if subscriber.unsubscribed:
        subscriber.unsubscribed = None
        subscriber.save(update_fields=['unsubscribed'])
