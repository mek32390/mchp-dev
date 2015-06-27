from django.contrib import admin
from . import models


class RosterEntryInline(admin.TabularInline):
    extra = 0
    fields = ('email', 'first_name', 'last_name', 'profile')
    ordering = ('profile', 'email')


class RosterEntryAdmin(admin.ModelAdmin):
    list_display = ('email', 'first_name', 'last_name', 'profile')
    fieldsets = (
        (None, {
            'fields': ['roster'],
        }),
        ('Personal information', {
            'fields': ['profile', 'email', 'first_name', 'last_name'],
        }),
    )


class RosterInstructorEntryInline(RosterEntryInline):
    model = models.RosterInstructorEntry


@admin.register(models.RosterInstructorEntry)
class RosterInstructorEntryAdmin(RosterEntryAdmin):
    pass


class RosterStudentEntryInline(RosterEntryInline):
    model = models.RosterStudentEntry


@admin.register(models.RosterStudentEntry)
class RosterStudentEntryAdmin(RosterEntryAdmin):
    pass


@admin.register(models.Roster)
class RosterAdmin(admin.ModelAdmin):
    inlines = [RosterStudentEntryInline, RosterInstructorEntryInline]
    list_display = ('course', 'created_by', 'when', 'approved', 'imported')
    fieldsets = (
        (None, {
            'fields': ['course', 'roster_html', 'emails'],
        }),
        ('Personal information', {
            'fields': ['created_by'],
        }),
        ('Important dates', {
            'fields': ['when', 'approved', 'imported'],
        }),
    )
    readonly_fields = ('when',)
