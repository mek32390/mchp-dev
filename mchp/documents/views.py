from allauth.account.decorators import verified_email_required

from django.contrib import messages
from django.core.urlresolvers import reverse
from django.http import HttpResponse
from django.shortcuts import render, get_object_or_404, redirect
from django.template import Context
from django.utils.decorators import method_decorator
from django.views.decorators.csrf import ensure_csrf_cookie
from django.views.generic.detail import DetailView
from django.views.generic.edit import FormView, DeleteView
from django.views.generic.list import ListView

from documents.forms import DocumentUploadForm
from documents.models import Document, Upload, DocumentPurchase
from documents.exceptions import DuplicateFileError
from schedule.models import Course

import json
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

        course_field = form.fields['course']

        course_field.queryset = Course.display_objects.filter(
            student__user = self.request.user
        ).order_by('dept', 'course_number', 'professor')
        course_field.empty_label = 'Pick a course'
        # the way the course is displayed in the dropdown , 
        # course.display comes from the model
        course_field.label_from_instance = lambda course: course.display()
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

    def get_context_data(self, **kwargs):
        context = super(DocumentListView, self).get_context_data(**kwargs)
        context['upload_count'] = Upload.objects.filter(owner=self.student).count()
        context['purchase_count'] = DocumentPurchase.objects.filter(student=self.student).count()
        # this kind of defeats the purpose of a list view, but eh
        purchases = DocumentPurchase.objects.filter(student=self.student)
        context['purchases'] = purchases

        return context

    @method_decorator(ensure_csrf_cookie)
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
    model = Document

    def get_object(self):
        return get_object_or_404(self.model, uuid=self.kwargs['uuid'])

    # this page is publically viewable 
    def dispatch(self, *args, **kwargs):
        return super(DocumentDetailPreview, self).dispatch(*args, **kwargs)

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

class AjaxableResponseMixin(object):
    """
    Mixin to add AJAX support to a form.

    I stole this right from the django website.
    """
    def render_to_json_response(self, context, **response_kwargs):
        data = json.dumps(context)
        response_kwargs['content_type'] = 'application/json'
        return HttpResponse(data, **response_kwargs)

    def ajax_messages(self):
        django_messages = []

        for message in messages.get_messages(self.request):
            django_messages.append({
                "level": message.level,
                "message": message.message,
                "extra_tags": message.tags,
            })
        return django_messages

class DocumentDeleteView(DeleteView, AjaxableResponseMixin):
    model = Document

    def get_success_url(self):
        return reverse('document_list')

    def get(self, request):
        return redirect(reverse('document_list'))

    def delete(self, request, *args, **kwargs):
        if self.request.is_ajax():
            if 'document' in request.POST:
                data = {}
                doc = Document.objects.filter(
                    pk=request.POST['document'],
                    upload__owner = self.student,
                )
                if not doc:
                    # incorrect pk, or doc belongs to someone else
                    messages.info(
                        self.request,
                        "Document not found."
                    )
                else:
                    # actually delete document
                    doc[0].delete()
                    messages.success(
                        self.request,
                        "Document deleted successfully."
                    )
            else:
                # no pk sent
                messages.error(
                    self.request,
                    "Document not specified."
                )
            data['messages'] =  self.ajax_messages()
            return self.render_to_json_response(data)
        else:
            return redirect(reverse('document_list'))


    @method_decorator(verified_email_required)
    @method_decorator(ensure_csrf_cookie)
    def dispatch(self, *args, **kwargs):
        self.student = self.request.user.student
        return super(DocumentDeleteView, self).dispatch(*args, **kwargs)

document_delete = DocumentDeleteView.as_view()
