from django.core.urlresolvers import reverse_lazy
from django.shortcuts import render

from django.views.generic import TemplateView
from django.views.generic.edit import FormView
from lib.decorators import school_required
from .forms import RosterUploadForm


class RosterUploadView(FormView):
    """ Upload a roster.

    """
    template_name = 'roster_upload.html'
    form_class = RosterUploadForm
    success_url = reverse_lazy('roster-upload-success')

    @school_required
    def dispatch(self, *args, **kwargs):
        super().dispatch(*args, **kwargs)

    def form_valid(self, form):
        # This method is called when valid form data has been POSTed.
        # It should return an HttpResponse.
        form.parse_roster()
        return super().form_valid(form)


class RosterUploadSuccessView(TemplateView):
    """ Roster uploaded successfully.

    """
    template_name = 'roster_upload_success.html'

    @school_required
    def dispatch(self, *args, **kwargs):
        super().dispatch(*args, **kwargs)
