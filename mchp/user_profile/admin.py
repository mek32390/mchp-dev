from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from django.contrib.auth.models import User
from django.db.models import get_models, get_app

from allauth.account.models import EmailAddress

from user_profile.models import Student, UserRole

for model in get_models(get_app('user_profile')):
    if model == Student:
        continue
    admin.site.register(model)

class StudentAdmin(admin.ModelAdmin):
    exclude = ('friends',)

admin.site.register(Student, StudentAdmin)

class StudentInline(admin.StackedInline):
    model = Student
    readonly_fields = ['school', 'major', 'friends']

class UserRoleInline(admin.StackedInline):
    model = UserRole

class EmailInline(admin.TabularInline):
    model = EmailAddress
    extra = 0

class CustomUserAdmin(UserAdmin):
    inlines = [
        StudentInline,
        UserRoleInline,
        EmailInline,
    ]
    list_filter = UserAdmin.list_filter + ('date_joined',)

admin.site.unregister(User)
admin.site.register(User, CustomUserAdmin)
