from django.contrib import admin
from django.db.models import get_models, get_app
from django import forms

from schedule.models import SchoolQuicklink, School, SchoolAlias, SchoolEmail

for model in get_models(get_app('schedule')):
    if model == SchoolAlias or model == SchoolEmail:
        continue
    admin.site.register(model)

class SchoolQuicklinkAdminForm(forms.ModelForm):
    domain = forms.ModelChoiceField(queryset=School.objects.order_by('name'))

    class Meta:
        model = SchoolQuicklink

class SchoolQuickLinkAdmin(admin.ModelAdmin):
    form = SchoolQuicklinkAdminForm

# admin.site.register(SchoolQuickLink, SchoolQuickLinkAdmin)

class SchoolAliasAdminForm(forms.ModelForm):
    domain = forms.ModelChoiceField(queryset=School.objects.order_by('name'))

    class Meta:
        model = SchoolAlias

class SchoolAliasAdmin(admin.ModelAdmin):
    form = SchoolAliasAdminForm

admin.site.register(SchoolAlias, SchoolAliasAdmin)

class SchoolEmailAdminForm(forms.ModelForm):
    school = forms.ModelChoiceField(queryset=School.objects.order_by('name'))

    class Meta:
        model = SchoolEmail

class SchoolEmailAdmi(admin.ModelAdmin):
    form = SchoolEmailAdminForm

admin.site.register(SchoolEmail, SchoolEmailAdmi)
