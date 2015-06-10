# from django.shortcuts import render
from django.core.urlresolvers import reverse_lazy

from django.views.generic.edit import CreateView
from lib.decorators import school_required
from . import models


class SyllabusCreate(CreateView):
    model = models.Syllabus
    fields = ['document', 'course']

    @school_required
    def dispatch(self, *args, **kwargs):
        super().dispatch(*args, **kwargs)


class RosterCreate(CreateView):
    model = models.Roster
    fields = ['html', 'course']

    template_name = 'roster_upload.html'
    # form_class = RosterUploadForm
    success_url = reverse_lazy('roster-upload-success')

    @school_required
    def dispatch(self, *args, **kwargs):
        super().dispatch(*args, **kwargs)


