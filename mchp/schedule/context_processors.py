def school(request):
    class no_school():
        def __init__(self):
            self.pk = 0
        def __str__(self):
            return 'Not a school'

    no_school_context = {
        'school': no_school()
    }

    if request.user.is_anonymous():
        return no_school_context
    if not request.user.student_exists():
        return no_school_context

    student = request.user.student
    context = {
        'user_school': student.school,
    }
    return context
