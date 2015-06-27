from django.contrib import admin
from . import models


class RosterEntryInline(admin.TabularInline):
    model = models.RosterEntry
    extra = 0
    fields = ('email', 'first_name', 'last_name', 'profile')
    ordering = ('profile', 'email')


@admin.register(models.RosterEntry)
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


@admin.register(models.Roster)
class RosterAdmin(admin.ModelAdmin):
    inlines = [RosterEntryInline]
    list_display = ('course', 'created_by', 'when', 'reviewed', 'imported')
    fieldsets = (
        (None, {
            'fields': ['course', 'roster_html', 'preview'],
        }),
        ('Personal information', {
            'fields': ['created_by'],
        }),
        ('Important dates', {
            'fields': ['when', 'approved', 'imported'],
        }),
    )
    readonly_fields = ('when',)
