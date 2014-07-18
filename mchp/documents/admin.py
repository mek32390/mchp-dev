from django.contrib import admin
from django.db.models import get_models, get_app
from django import forms

from documents.models import Document
from documents.widgets.admin import AdminDocThumnailWidget

for model in get_models(get_app('documents')):
    if model == Document:
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

class DocumentAdmin(admin.ModelAdmin):
    form = DocumentAdminForm

admin.site.register(Document, DocumentAdmin)
