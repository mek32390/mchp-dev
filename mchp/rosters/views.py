from django.core.urlresolvers import reverse_lazy
from django.views.generic.edit import FormView
from django.views.generic import DetailView
from django.utils.decorators import method_decorator
from lib.decorators import school_required
from schedule.models import Course
from . import forms, models, utils

# ensure is rep

class RosterSubmitView(FormView):
    template_name_suffix = '_create_form'
    form_class = forms.RosterSubmitForm
    success_url = reverse_lazy('roster-upload')

    def form_valid(self, form):
        # This method is called when valid form data has been POSTed.
        # It should return an HttpResponse.
        params = form.cleaned_data
        course_id = params.pop('course')
        instructor_emails = params.pop('emails')
        params['created_by'] = self.request.user.student_user
        params['course'] = Course.objects.get(pk=course_id)

        roster = models.Roster.objects.create(**params)

        # create roster entries
        for email in instructor_emails.split():
            models.RosterInstructorEntry.objects.create(email=email,
                                                        roster=form.instance)

        parsed_csv = utils.roster_html_to_csv(form.instance.roster_html)
        for initial_data in utils.csv_string_to_python(parsed_csv):
            params = {
                'first_name': initial_data.get('first'),
                'last_name': initial_data.get('last'),
                'email': initial_data.get('email'),
                'roster': roster,
            }
            models.RosterStudentEntry.objects.create(**params)

        return super().form_valid(form)

    @method_decorator(school_required)
    def dispatch(self, *args, **kwargs):
        return super().dispatch(*args, **kwargs)


class RosterDetailView(DetailView):
    # template_name_suffix = '_create_form'
    model = models.Roster
    # success_url = reverse_lazy('roster-upload')
    # fields = ['course', 'roster_html', 'emails']

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['course'] = self.get_object().course
        return context

    @method_decorator(school_required)
    def dispatch(self, *args, **kwargs):
        return super().dispatch(*args, **kwargs)
