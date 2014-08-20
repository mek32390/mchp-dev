from django.contrib import admin
from django.db.models import get_models, get_app
from django import forms

from schedule.models import SchoolQuicklink, School, Department

for model in get_models(get_app('schedule')):
    if model == SchoolQuicklink:
        continue
    if model == Department:
        continue
    admin.site.register(model)

class DepartmentAdminForm(forms.ModelForm):
    name = forms.ModelChoiceField(queryset=Department.objects.order_by('name'))

    class Meta:
        model = Department

class DepartmentAdmin(admin.ModelAdmin):
    form = DepartmentAdminForm

admin.site.register(Department, DepartmentAdmin)

class SchoolQuicklinkAdminForm(forms.ModelForm):
    domain = forms.ModelChoiceField(queryset=School.objects.order_by('name'))

    class Meta:
        model = SchoolQuicklink

class SchoolQuickLinkAdmin(admin.ModelAdmin):
    form = SchoolQuicklinkAdminForm

admin.site.register(SchoolQuicklink, SchoolQuickLinkAdmin)
