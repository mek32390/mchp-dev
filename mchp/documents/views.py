from django.contrib import messages
from django.conf import settings
from django.core import serializers
from django.core.urlresolvers import reverse
from django.db.models import Count
from django.http import HttpResponse, HttpResponseNotAllowed
from django.shortcuts import render, get_object_or_404, redirect
from django.utils import timezone
from django.utils.decorators import method_decorator
from django.views.decorators.csrf import ensure_csrf_cookie
from django.views.generic.detail import DetailView
from django.views.generic.edit import FormView, DeleteView, UpdateView, View
from django.views.generic.list import ListView

from documents.forms import DocumentUploadForm
from documents.models import Document, Upload, DocumentPurchase
from documents.exceptions import DuplicateFileError
from calendar_mchp.models import ClassCalendar, CalendarEvent
from lib.decorators import school_required
from referral.models import ReferralCode
from schedule.models import Course

from decimal import Decimal, ROUND_HALF_DOWN
import json
import logging
logger = logging.getLogger(__name__)

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

'''
url: add/
name: document_upload
'''
class DocumentFormView(FormView, AjaxableResponseMixin):
    template_name = 'documents/upload.html'
    form_class = DocumentUploadForm

    def get_success_url(self):
        return reverse('document_list')

    def get(self, request, *args, **kwargs):
        form_class = self.get_form_class()
        form = self.get_form(form_class)
        course_field = form.fields['course']
        event_field = form.fields['event']

        enrolled_courses = Course.objects.get_courses_for(self.student)

        course_field.queryset = enrolled_courses
        course_field.empty_label = 'Pick a course'

        event_field.empty_label = 'Pick an event'
        student_events = CalendarEvent.objects.filter(
            calendar__owner=self.student,
            calendar__course__in=enrolled_courses
        ).values('id', 'title', 'calendar__course')

        student_course_events = dict()
        for event in student_events:
            course_id = event['calendar__course']
            if course_id not in student_course_events:
                student_course_events[course_id] = []

            student_course_events[course_id].append(event)

        type_field = form.fields['type']
        type_field.queryset = Document.DOCUMENT_TYPE_CHOICES

        # course.display comes from the model
        course_field.label_from_instance = lambda course: course.display()

        data = {
            'enrolled_courses': enrolled_courses,
            'student_course_events_serialized': json.dumps(student_course_events),
            'form': form,
        }

        return render(request, self.template_name, data)

    def post(self, request, *args, **kwargs):
        form_class = self.get_form_class()
        form = self.get_form(form_class)

        # Updating event query set
        course_id = request.POST.get('course', None)
        if course_id:
            events = CalendarEvent.objects.filter(calendar__owner=self.student, calendar__course__id=course_id)
            form.fields['event'].queryset = events

        if form.is_valid():
            return self.form_valid(form)
        else:
            return self.form_invalid(form)

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

        upload = Upload(document=doc, owner=self.student)
        upload.save()

        event = form.cleaned_data.get('event', None)
        if event:
            event.documents.add(doc)

        messages.success(
            self.request,
            "Upload successful"
        )
        return super(DocumentFormView, self).form_valid(form)

    @method_decorator(school_required)
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
    model = Document

    def get_queryset(self):
        return Document.objects.filter(upload__owner=self.student).order_by('-create_date').annotate(
            purchase_count = Count('purchased_document'),
        ).extra(select = {
            # can't filter on annotations so get the count manually
            'review_count': 'SELECT COUNT(*) FROM "documents_documentpurchase"'+\
            'WHERE ("documents_documentpurchase"."document_id" = "documents_document"."id"'+\
            'AND NOT ("documents_documentpurchase"."review_date" IS NULL))',
        })

    def get_context_data(self, **kwargs):
        context = super(DocumentListView, self).get_context_data(**kwargs)
        context['upload_count'] = Upload.objects.filter(owner=self.student).count()
        context['purchase_count'] = DocumentPurchase.objects.filter(student=self.student).count()
        # this kind of defeats the purpose of a list view, but eh
        purchases = Document.objects.filter(purchased_document__student=self.student).select_related().order_by('title').annotate(
            purchase_count = Count('purchased_document')
        ).extra(select = {
            'review_count': 'SELECT COUNT(*) FROM "documents_documentpurchase"'+\
            'WHERE ("documents_documentpurchase"."document_id" = "documents_document"."id"'+\
            'AND NOT ("documents_documentpurchase"."review_date" IS NULL))'
        })
        context['purchases'] = purchases
        context['now'] = timezone.now()

        return context

    @method_decorator(ensure_csrf_cookie)
    @method_decorator(school_required)
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

    def post(self, request, *args, **kwargs):
        # for users who are not logged in
        if not self.student:
            return redirect(reverse('landing_page'))

        document = self.get_object()
        # if they already bought the doc
        uploader = Upload.objects.filter(document=document)
        if uploader.exists():
            uploader = uploader[0].owner
            uploader_pk = uploader.pk
        else:
            uploader = None
            uploader_pk = -1
        if DocumentPurchase.objects.filter(document=document, student=self.student).exists() or\
           uploader_pk == self.student.pk:
           # or they uploaded it themselves, redirect to the view of the doc
            return redirect(reverse('document_list') + self.kwargs['uuid'] + '/' + document.slug)


        points_left = self.student.reduce_points(document.price)
        if points_left is None:
            # student didn't have enough points
            messages.error(
                request,
                "Pump your breaks kid, you don't have enough points to buy that."
            )
        else:
            # student bought the doc
            purchase = DocumentPurchase(document=document, student=self.student)
            purchase.save()
            # give uploader the points, if they exist
            if uploader:
                points = document.price * (settings.MCHP_PRICING['commission_rate'] / 100)
                points = points / 100
                points = Decimal(points).quantize(Decimal('1.0000'), rounding=ROUND_HALF_DOWN)
                uploader.modify_balance(points)
                uploader.save()

        return redirect(reverse('document_list') + self.kwargs['uuid'] + '/' + document.slug)

    def get(self, request, *args, **kwargs):
        # parent stuff, getting object
        self.object = self.get_object()
        context = self.get_context_data(object=self.object)

        # info about the document
        uploader = Upload.objects.filter(document=self.object)
        if uploader.exists():
            uploader = uploader[0].owner
        else:
            uploader = None

        document = self.get_object()
        owns = False
        referral_link = ''
        if not request.user.is_anonymous() and request.user.student_exists():
            referral_link = ReferralCode.objects.get_referral_code(request.user).referral_link
            # check if they already bought the doc
            uploader = Upload.objects.filter(document=document)
            if uploader.exists():
                uploader = uploader[0].owner
                uploader_pk = uploader.pk
            else:
                uploader = None
                uploader_pk = -1
            if DocumentPurchase.objects.filter(document=document, student=self.student).exists() or\
               uploader_pk == self.student.pk:
                owns = True

        cals = ClassCalendar.objects.filter(
            owner=uploader
        ).count()
        docs = Upload.objects.filter(
            owner=uploader
        ).count()
        all_counts = cals + docs
        if all_counts == 0:
            all_counts = 1
        context['cal_percent'] = (cals * 100) / all_counts
        context['doc_percent'] = (docs * 100) / all_counts
        if uploader:
            docs_sold = uploader.sales()
        else:
            docs_sold = 0

        document_preview_flag = 'document preview referral'
        flag = self.student.one_time_flag.get_flag(self.student, document_preview_flag) if self.student else False
        data = {
            'current_path': request.get_full_path(),
            'docs_sold': docs_sold, 
            'uploader': uploader,
            'student': self.student,
            'reviews': self.object.purchased_document.exclude(review_date=None).exclude(review__exact=''),
            'review_count':
            self.object.purchased_document.exclude(review_date=None).exclude(review__exact='').count(),
            'uuid': self.kwargs['uuid'],
            'slug': self.object.slug,
            'owns': owns,
            'referral_link': referral_link,
            'referral_reward': settings.MCHP_PRICING['referral_reward'],
            'document_preview_flag': flag, 
            'document_preview_flag_name': document_preview_flag,
        }
        context.update(data)
        return self.render_to_response(context)

    def get_object(self):
        logger.debug(self.kwargs['uuid'])
        return get_object_or_404(self.model, uuid=self.kwargs['uuid'])

    # this page is publically viewable 
    def dispatch(self, *args, **kwargs):
        if not self.request.user.is_anonymous() and self.request.user.student_exists():
            self.student = self.request.user.student
        else:
            self.student = None
        return super(DocumentDetailPreview, self).dispatch(*args, **kwargs)

document_preview = DocumentDetailPreview.as_view()

'''
url: <uuid>/slug
name: document_detail
'''
class DocumentDetailView(DetailView):
    template_name = 'documents/view.html'
    model = Document

    def post(self, request, *args, **kwargs):
        return HttpResponseNotAllowed(['GET'])

    @method_decorator(school_required)
    def get(self, request, *args, **kwargs):
        # parent stuff, getting the object
        self.object = self.get_object()
        context = self.get_context_data(object=self.object)

        # check if user bought the doc
        purchased = DocumentPurchase.objects.filter(document=self.object,
                                                    student=self.student).exists()
        # or if they own the doc
        upload = Upload.objects.filter(document=self.object)
        if upload.exists():
            owner = upload[0].owner
            owner_pk = owner.pk
        else:
            owner = None
            owner_pk = -1

        # if not, redirect to the preview page
        if not purchased and owner_pk != self.student.pk:
            return redirect(reverse('document_list') + 'preview/' + self.kwargs['uuid'] + '/' +
                            self.object.slug)
        # check if they have reviewed it
        reviewed = False
        if purchased:
            reviewed = DocumentPurchase.objects.filter(document=self.object,
                                                    student=self.student).values_list('review_date',
                                                                                     flat=True)[0]
        # it they uploaded it or already reviewed it, they shouldn't be able to rate it again
        rated = False
        if owner == self.student.pk or reviewed != None:
            rated = True
        context['rated'] = rated
        context['current_path'] = request.get_full_path()
        return self.render_to_response(context)

    def get_object(self):
        return get_object_or_404(self.model, uuid=self.kwargs['uuid'])

    def get_context_data(self, **kwargs):
        context = super(DocumentDetailView, self).get_context_data(**kwargs)
        context['uuid'] = self.kwargs['uuid']
        context['slug'] = self.object.slug
        context['student'] = self.student 
        context['referral_link'] = self.referral_link
        context['referral_reward'] = settings.MCHP_PRICING['referral_reward']
        document_referral_flag = 'document referral'
        context['document_referral_flag'] = self.student.one_time_flag.get_flag(self.student, document_referral_flag)
        context['document_referral_flag_name'] = document_referral_flag
        return context

    # this page needs to be publically viewable to redirect properly
    def dispatch(self, *args, **kwargs):
        if not self.request.user.is_anonymous() and self.request.user.student_exists():
            self.student = self.request.user.student
            self.referral_link = ReferralCode.objects.get_referral_code(self.student.user).referral_link
            return super(DocumentDetailView, self).dispatch(*args, **kwargs)
        else:
            return redirect(reverse('document_list') + 'preview/' + self.kwargs['uuid'])

document_detail = DocumentDetailView.as_view()

'''
url: remove/
name: document_delete
'''
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
                    messages.error(
                        self.request,
                        "Document not found."
                    )
                    data['messages'] =  self.ajax_messages()
                    return self.render_to_json_response(data, status=403)
                else:
                    # delete upload and purchases
                    doc = doc[0]
                    doc.upload.delete()
                    doc.purchased_document.all().delete()
                    # actually delete document
                    doc.delete()
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
            return self.render_to_json_response(data, status=200)
        else:
            return redirect(reverse('document_list'))


    @method_decorator(school_required)
    @method_decorator(ensure_csrf_cookie)
    def dispatch(self, *args, **kwargs):
        self.student = self.request.user.student
        return super(DocumentDeleteView, self).dispatch(*args, **kwargs)

document_delete = DocumentDeleteView.as_view()

'''
url: unpurchase/
name: purchase_delete
'''
class PurchaseDeleteView(DeleteView, AjaxableResponseMixin):
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
                )
                purchase = DocumentPurchase.objects.filter(document=doc, student=self.student)
                if not purchase.exists():
                    # they didn't buy this doc
                    messages.error(
                        self.request,
                        "Purchased Document not found."
                    )
                    data['messages'] =  self.ajax_messages()
                    return self.render_to_json_response(data, status=403)
                else:
                    # delete purchase record
                    purchase[0].delete()
                    messages.success(
                        self.request,
                        "Document removed successfully."
                    )
            else:
                # no pk sent
                messages.error(
                    self.request,
                    "Document not specified."
                )
            data['messages'] =  self.ajax_messages()
            return self.render_to_json_response(data, status=200)
        else:
            return redirect(reverse('document_list'))

    @method_decorator(school_required)
    @method_decorator(ensure_csrf_cookie)
    def dispatch(self, *args, **kwargs):
        self.student = self.request.user.student
        return super(PurchaseDeleteView, self).dispatch(*args, **kwargs)

purchase_delete = PurchaseDeleteView.as_view()

'''
url: review/
name: purchase_update
'''
class PurchaseUpdateView(UpdateView, AjaxableResponseMixin):
    model = DocumentPurchase

    def get_success_url(self):
        return reverse('document_list')

    def get(self, request):
        return redirect(reverse('document_list'))

    def post(self, request, *args, **kwargs):
        if self.request.is_ajax():
            if 'document' in request.POST:
                data = {}
                #FIXME this should probably be a filter?
                purchase = DocumentPurchase.objects.get(
                    document__id=request.POST['document'],
                    student = self.student,
                )
                if not purchase:
                    # they didn't buy this doc
                    messages.error(
                        self.request,
                        "You can't review a document you have not purchased."
                    )
                    data['messages'] =  self.ajax_messages()
                    return self.render_to_json_response(data, status=403)
                else:
                    # if review_date exists, document was already reviewed
                    if purchase.review_date:
                        messages.warning(
                            self.request,
                            "You have already reviewed this document."
                        )
                        data['messages'] =  self.ajax_messages()
                        return self.render_to_json_response(data, status=200)

                    # add a review to the purchase record
                    review = request.POST['review'][:250]
                    purchase.review = review

                    # add vote to document record
                    vote = int(request.POST['vote'])
                    if vote == 0:
                        purchase.document.down = purchase.document.down + 1
                    elif vote == 1:
                        purchase.document.up = purchase.document.up + 1
                    else:
                        messages.error(
                            self.request,
                            "Vote not valid"
                        )
                        data['messages'] =  self.ajax_messages()
                        return self.render_to_json_response(data, status=403)
                    messages.success(
                        self.request,
                        "Document reviewed successfully."
                    )
                    # add time stamp
                    purchase.review_date = timezone.now()

                    # save models
                    purchase.save()
                    purchase.document.save()
            else:
                # no pk sent
                messages.error(
                    self.request,
                    "Document not specified."
                )
            data['messages'] =  self.ajax_messages()
            return self.render_to_json_response(data, status=200)
        else:
            return redirect(reverse('document_list'))

    @method_decorator(school_required)
    def dispatch(self, *args, **kwargs):
        self.student = self.request.user.student
        return super(PurchaseUpdateView, self).dispatch(*args, **kwargs)

purchase_update = PurchaseUpdateView.as_view()

'''
url: fetch-preview/
name: fetch_preview
'''
class FetchPreview(View, AjaxableResponseMixin):
    model = Document

    def post(self, request, *args, **kwargs):
        return HttpResponseNotAllowed(['GET'])

    def get(self, request, *args, **kwargs):
        if self.request.is_ajax():
            data = {}
            if 'document' in request.GET:
                document = Document.objects.filter(
                    id=request.GET['document'],
                    upload__owner = self.student,
                )
                if not document.exists():
                    # couldn't find the document
                    data['found'] = False
                    return self.render_to_json_response(data, status=403)
                else:
                    document = document[0]
                    # the preview has been created
                    if document.preview:
                        data['thumbnail_url'] = document.preview.url
                        data['document_title'] = document.title
                        data['price'] = document.price
                        data['document_url'] = request.get_host() + reverse('document_list') + \
                                document.uuid + '/' + \
                                document.slug
                        data['found'] = True
                        return self.render_to_json_response(data, status=200)
                    else:
                        # the preview has not yet been created
                        data['found'] = False
                        return self.render_to_json_response(data, status=200)

            else:
                # no pk sent
                data['found'] = False
                return self.render_to_json_response(data, status=403)
        else:
            return redirect(reverse('document_list'))

    @method_decorator(school_required)
    def dispatch(self, *args, **kwargs):
        self.student = self.request.user.student
        return super(FetchPreview, self).dispatch(*args, **kwargs)

fetch_preview = FetchPreview.as_view()
