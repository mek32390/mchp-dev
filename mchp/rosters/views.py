from django.core.urlresolvers import reverse_lazy
from django.views.generic.edit import FormView, UpdateView
from django.utils.decorators import method_decorator
from lib.decorators import school_required
from documents.exceptions import DuplicateFileError
from django.contrib import messages
from documents.models import Document, Upload, DocumentPurchase
from django.forms.formsets import formset_factory

from schedule.models import Course
from . import forms, models, utils


class RosterSubmitView(FormView):
    """ Submit a new roster.

    Notes
    -----
    [TODO] this should ensure user is rep/intern

    """
    template_name = 'rosters/roster_submit_form.html'
    form_class = forms.RosterSubmitForm
    success_url = reverse_lazy('roster-upload')

    def post(self, request, *args, **kwargs):
        form_class = self.get_form_class()
        form = self.get_form(form_class)

        eventset = forms.RosterEventFormSet(request.POST)

        if form.is_valid():
            form.cleaned_data['events'] = eventset
            return self.form_valid(form)
        else:
            return self.form_invalid(form, **kwargs)

    def form_valid(self, form):
        # This method is called when valid form data has been POSTed.
        # It should return an HttpResponse.
        course_id = form.cleaned_data['course']
        course_name = form.cleaned_data['course_name']
        roster_html = form.cleaned_data['roster_html']
        instructor_emails = form.cleaned_data['emails'].split()
        document = form.cleaned_data['document']
        events = form.cleaned_data['events']

        params = {
            'roster_html': roster_html,
            'created_by': self.request.user.student_user,
            'course': Course.objects.get(pk=course_id)
        }

        roster = models.Roster.objects.create(**params)

        if events.is_valid():
            for event in events.cleaned_data:
                print(event)
                params = {
                    'title': event['title'],
                    'date': event['date'],
                    'roster': roster
                }
            models.RosterEventEntry.objects.create(**params)


        # create roster entries
        for email in instructor_emails:
            params = {
                'email': email,  # utils.preprocess_email(email),
                'roster': roster,
                'approved': False
            }
            user = utils.get_user(email)
            if user:
                params['profile'] = user.profile_user
            models.RosterInstructorEntry.objects.create(**params)

        try:
            doc = Document(type=Document.SYLLABUS, title='Course Syllabus for ' + course_name,
                           description='Course Syllabus for ' + course_name,
                           document=document, course_id=None, approved=False, roster=roster)
            doc.save()
        except DuplicateFileError as err:
            messages.error(
                self.request,
                err
            )
            return self.get(self.request)

        upload = Upload(document=doc, owner=self.student)
        upload.save()
        messages.success(
            self.request,
            "Syllabus upload successful"
        )

        return super().form_valid(form)

    @method_decorator(school_required)
    def dispatch(self, *args, **kwargs):
        self.student = self.request.user.student
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

    # TODO: implement document_uploaded signal for syllabus upon doc approval

    def get_success_url(self):
        return reverse_lazy('roster-review', args=[self.object.pk])

    # def get_context_data(self, **kwargs):
    #     context = super().get_context_data(**kwargs)
    #     context['course'] = self.get_object().course
    #     return context

    @method_decorator(school_required)
    def dispatch(self, *args, **kwargs):
        return super().dispatch(*args, **kwargs)
