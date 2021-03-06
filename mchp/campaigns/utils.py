from django.core.mail import EmailMultiAlternatives
from django.http import HttpResponse
from django.shortcuts import redirect
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


def beacon_response():
    """ Subscriber opened an e-mail.

    Notes
    -----
    This is here to allow CampaignSubscriber subclasses to use this feature.

    """
    response = HttpResponse()
    response.status_code = 204
    return response


def handle_click(subscriber, url):
    """ Subscriber clicked through from an e-mail.

    Parameters
    ----------
    subscriber : data-type
        A subscriber object.
    url : str
        A URL to which to redirect.

    Notes
    -----
    This is here to allow CampaignSubscriber subclasses to use this feature.

    """
    return redirect(url)
