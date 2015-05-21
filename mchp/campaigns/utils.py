from django.core.mail import EmailMultiAlternatives
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


def beacon():
    try:
        # [TODO] don't hardcode this
        valid_image = "campaigns/static/campaigns/beacon.png"
        with open(valid_image, "rb") as f:
            return f.read()
    except IOError:
        pass
    return None
