from django.shortcuts import render


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


def ensure_user_exists(email, fname=None, lname=None):
    """ Return an existing user associated with a given e-mail address.

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
    ValueError
        If the given e-mail address is blank, `None`, or otherwise "falsy."

    Notes
    -----
    This searches not only the user model e-mail address, but also the
    addresses specified in the AllAuth inline.

    """
    from django.contrib.auth.models import User
    email = User.objects.normalize_email(email)
    if not email:
        raise ValueError('A valid e-mail address must be specified')

    try:
        user = User.objects.get(email=email)
    except User.DoesNotExist:
        # [TODO] check inline e-mail addresses, as well
        username = None  # [TODO] generate
        params = {}
        if fname:
            params['first_name'] = fname
        if lname:
            params['last_name'] = fname
        user = User.objects.create_user(username, None, email, **params)
    return user
