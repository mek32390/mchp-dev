from django.contrib import admin
from django.db.models import get_models, get_app
from django import forms

from documents.models import Document, Upload
from documents.widgets.admin import AdminDocThumnailWidget

for model in get_models(get_app('documents')):
    if model == Document or model == Upload:
        continue
    admin.site.register(model)

# I stole this from 
# http://www.yaconiello.com/blog/auto-generating-pdf-covers-on-upload-django-and-imagemagick/
class DocumentAdminForm(forms.ModelForm):
    class Meta:
        model = Document
        widgets = {
            'preview' : AdminDocThumnailWidget(),
        }

class DocumentUploadInline(admin.StackedInline):
    model = Upload

class DocumentAdmin(admin.ModelAdmin):
    form = DocumentAdminForm
    search_fields = ['title']
    readonly_fields = ['uuid', 'md5sum', 'filetype']
    inlines = [
        DocumentUploadInline,
    ]

admin.site.register(Document, DocumentAdmin)

class UploadAdmin(admin.ModelAdmin):
    search_fields = [
        'document__title', 
        'owner__user__username',
    ]

admin.site.register(Upload, UploadAdmin)
