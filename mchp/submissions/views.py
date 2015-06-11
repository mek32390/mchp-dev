# from django.shortcuts import render
from django.core.urlresolvers import reverse_lazy
from django.views.generic.edit import FormView
from lib.decorators import school_required
from . import forms


class CourseSetUploadView(FormView):
    template_name = 'documents/upload.html'
    form_class = forms.CourseSetForm
    success_url = reverse_lazy('course-set-upload-success')

    def form_valid(self, form):
        # This method is called when valid form data has been POSTed.
        # It should return an HttpResponse.
        form.make_models()
        return super().form_valid(form)

    @school_required
    def dispatch(self, *args, **kwargs):
        super().dispatch(*args, **kwargs)
