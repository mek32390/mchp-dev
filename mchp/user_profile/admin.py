from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from django.contrib.auth.models import User
from django.db.models import get_models, get_app

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
    exclude = ('friends', 'school', 'major')

class UserRoleInline(admin.StackedInline):
    model = UserRole

class CustomUserAdmin(UserAdmin):
    inlines = [
        StudentInline,
        UserRoleInline,
    ]

admin.site.unregister(User)
admin.site.register(User, CustomUserAdmin)
