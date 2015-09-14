from django.core.urlresolvers import reverse_lazy
from django.views.generic.edit import FormView, UpdateView
from django.utils.decorators import method_decorator
from lib.decorators import school_required
from schedule.models import Course
from . import forms, models, utils
from mchp.lib.decorators import intern_manager_required, rep_required


class RosterSubmitView(FormView):
    """ Submit a new roster.

    Notes
    -----
    [TODO] this should ensure user is rep/intern

    """
    template_name = 'rosters/roster_submit_form.html'
    form_class = forms.RosterSubmitForm
    success_url = reverse_lazy('roster-upload')

    def form_valid(self, form):
        # This method is called when valid form data has been POSTed.
        # It should return an HttpResponse.
        course_id = form.cleaned_data['course']
        roster_html = form.cleaned_data['roster_html']
        instructor_emails = form.cleaned_data['emails'].split()

        params = {
            'roster_html': roster_html,
            'created_by': self.request.user.student_user,
            'course': Course.objects.get(pk=course_id),
        }

        roster = models.Roster.objects.create(**params)

        # create roster entries
        for email in instructor_emails:
            params = {
                'email': utils.preprocess_email(email),
                'roster': roster,
            }
            user = utils.get_user(email)
            if user:
                params['profile'] = user.profile_user
            models.RosterInstructorEntry.objects.create(**params)

        parsed_csv = utils.roster_html_to_csv(roster_html)
        for initial_data in utils.csv_string_to_python(parsed_csv):
            # n.b.: emails from instructor emails are not filtered here
            email = initial_data.get('email')
            # don't add entry if email is in instructors
            if email not in instructor_emails:
                params = {
                    'first_name': initial_data.get('first'),
                    'last_name': initial_data.get('last'),
                    'email': utils.preprocess_email(email),
                    'roster': roster,
                }
                user = utils.get_user(email)
                if user:
                    params['profile'] = user.profile_user
                models.RosterStudentEntry.objects.create(**params)

        return super().form_valid(form)

    @method_decorator(rep_required)
    def dispatch(self, *args, **kwargs):
        return super().dispatch(*args, **kwargs)


class RosterReviewView(UpdateView):
    """ Review a submitted roster.

    Notes
    -----
    As with the submit view, this should verify permissions.

    """
    model = models.Roster
    fields = ['status']
    template_name_suffix = '_review_form'

    def get_success_url(self):
        return reverse_lazy('roster-review', args=[self.object.pk])

    # def get_context_data(self, **kwargs):
    #     context = super().get_context_data(**kwargs)
    #     context['course'] = self.get_object().course
    #     return context

    @method_decorator(intern_manager_required)
    def dispatch(self, *args, **kwargs):
        return super().dispatch(*args, **kwargs)