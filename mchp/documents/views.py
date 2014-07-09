from allauth.account.decorators import verified_email_required

from django.shortcuts import render, get_object_or_404
from django.core.urlresolvers import reverse
from django.views.generic.list import ListView
from django.views.generic.edit import FormView 
from django.views.generic.detail import DetailView
from django.utils.decorators import method_decorator
from django.template import Context
from django.contrib import messages

from documents.forms import DocumentUploadForm
from documents.models import Document, Upload
from documents.exceptions import DuplicateFileError

import logging
logger = logging.getLogger(__name__)

'''
url: add/
name: document_upload
'''
class DocumentFormView(FormView):
    template_name = 'documents/upload.html'
    form_class = DocumentUploadForm

    def get_success_url(self):
        return reverse('document_list')

    def get(self, request, *args, **kwargs):
        form_class = self.get_form_class()
        form = self.get_form(form_class)

        data = {

        }
        context_data = Context(self.get_context_data(form=form))
        context_data.update(data)
        return render(request, self.template_name, context_data)

    def form_invalid(self, form):
        messages.error(
            self.request,
            "Upload failed."
        )
        return self.get(self.request)

    def form_valid(self, form):
        try:
            doc = form.save()
        except DuplicateFileError as err:
            messages.error(
                self.request,
                err
            )
            return self.get(self.request)
        messages.success(
            self.request,
            "Upload successful"
        )

        upload = Upload(document=doc, owner=self.student)
        upload.save()
        return super(DocumentFormView, self).form_valid(form)


    @method_decorator(verified_email_required)
    def dispatch(self, *args, **kwargs):
        self.student = self.request.user.student
        return super(DocumentFormView, self).dispatch(*args, **kwargs)

document_upload = DocumentFormView.as_view()

'''
url: /
name: document_list
'''
class DocumentListView(ListView):
    template_name = 'documents/list.html'
    model = Upload

    def get_queryset(self):
        return Upload.objects.filter(owner=self.student).select_related()

    @method_decorator(verified_email_required)
    def dispatch(self, *args, **kwargs):
        self.student = self.request.user.student
        return super(DocumentListView, self).dispatch(*args, **kwargs)

document_list = DocumentListView.as_view()

'''
url: preview/<uuid>/slug
name: document_preview
'''
class DocumentDetailPreview(DetailView):
    template_name = 'documents/preview.html'

    def get_queryset(self):
        return Document.objects.all()[0]

    # this page is publically viewable 
    def dispatch(self, *args, **kwargs):
        return super(DocumentFormView, self).dispatch(*args, **kwargs)

document_preview = DocumentDetailPreview.as_view()

'''
url: <uuid>/slug
name: document_detail
'''
class DocumentDetailView(DetailView):
    template_name = 'documents/view.html'
    model = Document

    def get_object(self):
        return get_object_or_404(self.model, uuid=self.kwargs['uuid'])

    def get_context_data(self, **kwargs):
        context = super(DocumentDetailView, self).get_context_data(**kwargs)
        context['what'] = self.kwargs['uuid']
        return context

    @method_decorator(verified_email_required)
    def dispatch(self, *args, **kwargs):
        self.student = self.request.user.student
        return super(DocumentDetailView, self).dispatch(*args, **kwargs)

document_detail = DocumentDetailView.as_view()
