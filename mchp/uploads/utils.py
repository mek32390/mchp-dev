from django.contrib.auth.models import User

def parse_roster(html):
    """ Parse an HTML roster into a collection of users.

    Parameters
    ----------
    html : str
        HTML data to parse.

    Returns
    -------
    out : list of dict
        A collection of parsed items.

    """
    out = []
    # [TODO] flesh me out
    return out


def ensure_enrollment_exists(course, student, receive_email=True):
    """ Enroll a student if not already enrolled.

    Parameters
    ----------
    course : schedule.models.Course
        A course in which to enroll a student.
    student : user_profile.models.Student
        A student to enroll in a course.
    receive_email : bool, optional
        Should a new enrollee receive e-mail?  Default `True`.
        Has no effect if enrollment already exists.

    Returns
    -------
    out : schedule.models.Enrollment
        A new or existing enrollment record for a student in the given course.

    """
    from schedule.models import Enrollment
    enrollment, _ = Enrollment.objects.get_or_create(
        course=course,
        student=student,
        defaults={'receive_email': receive_email})
    return enrollment


def ensure_student_exists(school, user):
    """ Create a student if they don't already exist.

    Parameters
    ----------
    school : schedule.models.School
        A school at which to create a student.
    user : django.conf.settings.AUTH_USER_MODEL
        A user for which to create a student.

    Returns
    -------
    out : user_profile.models.Student
        A new or existing student.

    """
    from user_profile.models import Student
    student = user.student_user
    if not student:
        student = Student.objects.create_student(user, school)
    return student


def numeric_suffix(s, suffix, max_length):
    """ Take a string and replace the end with a suffix.

    Parameters
    ----------
    s : str
        A string to suffix.
    suffix : str
        A stuffix for the string.
    max_length : int
        The maximum allowed length.

    Raises
    ------
    ValueError
        If length of `suffix` exceeds `max_length`.

    Notes
    -----
    Some examples:

        joe.q.public, '', 8 => joe.q.pu
        joe.q.public, 'jr', 8 => joe.q.jr
        joe.q.public, 'jr', 8 => joe.q.jr
        joe.q.public, '', 20 => joe.q.public
        joe.q.public, 'jr', 20 => joe.q.publicjr

    """
    suffix_len = len(suffix)
    if suffix_len > max_length:
        raise ValueError('Suffix length cannot exceed max length')
    return s[:max_length - suffix_len] + suffix


def make_username(email):
    """ Generate a non-duplicate username.

    Parameters
    ----------
    email : str
        An e-mail address to process

    Returns
    -------
    out : str
        The created username.

    """
    MAX_HANDLE_LEN = 30
    from itertools import count
    handle, _ = email.split('@')[:MAX_HANDLE_LEN]
    c = count(1)
    while True:
        try:
            User.objects.get(username__iexact=handle)
        except User.DoesNotExist:
            break
        else:
            handle = numeric_suffix(handle, str(next(c)), MAX_HANDLE_LEN)
    return handle


def ensure_user_exists(email, fname=None, lname=None):
    """ Find or create a user associated with a given e-mail address.

    Parameters
    ----------
    email : str
        An e-mail address associated with the user.
    fname : str, optional
        An optional first name for the user.
    lname : str, optional
        An optional last name for the user.

    Returns
    -------
    out : django.conf.settings.AUTH_USER_MODEL
        A new or existing user.

    Raises
    ------
    ValidationError
        If the given e-mail fails validation.

    Notes
    -----
    This searches not only the user model e-mail address, but also the
    addresses specified in the AllAuth inline.

    """
    from django.core.validators import validate_email
    from django.allauth.models import EmailAddress

    email = User.objects.normalize_email(email)
    validate_email(email)

    try:
        user = User.objects.get(email__iexact=email)
    except User.DoesNotExist:
        try:
            user = EmailAddress.objects.get(email__iexact=email).user
        except EmailAddress.DoesNotExist:
            username = make_username(email)
            params = {}
            if fname:
                params['first_name'] = fname
            if lname:
                params['last_name'] = fname
            user = User.objects.create_user(username, None, email, **params)
    return user
