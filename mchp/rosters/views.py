from django.core.urlresolvers import reverse_lazy
from django.views.generic.edit import CreateView
from django.views.generic import DetailView
from django.utils.decorators import method_decorator
from lib.decorators import school_required
from . import models, utils


class RosterCreateView(CreateView):
    template_name_suffix = '_create_form'
    model = models.Roster
    success_url = reverse_lazy('roster-upload')
    fields = ['course', 'roster_html', 'emails']

    def form_valid(self, form):
        # This method is called when valid form data has been POSTed.
        # It should return an HttpResponse.

        form.instance.created_by = self.request.user.student_user
        valid = super().form_valid(form)

        # create roster entries
        for email in form.instance.emails.split():
            models.RosterInstructorEntry.objects.create(email=email,
                                                        roster=form.instance)

        parsed_csv = utils.roster_html_to_csv(form.instance.roster_html)
        for initial_data in utils.csv_string_to_python(parsed_csv):
            params = {
                'first_name': initial_data.get('first'),
                'last_name': initial_data.get('last'),
                'email': initial_data.get('email'),
                'roster': form.instance,
            }
            models.RosterStudentEntry.objects.create(**params)

        return valid

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
