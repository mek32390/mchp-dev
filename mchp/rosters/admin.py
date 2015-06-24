from django.contrib import admin
from . import models


@admin.register(models.Roster)
class RosterAdmin(admin.ModelAdmin):
    list_display = ('course', 'created_by', 'when', 'approved', 'imported')
    fieldsets = (
        (None, {
            'fields': ['course', 'roster_html', 'parsed_csv', 'preview'],
        }),
        ('Personal information', {
            'fields': ['created_by'],
        }),
        ('Important dates', {
            'fields': ['when', 'approved', 'imported'],
        })
    )
    readonly_fields = ('when', 'parsed_csv', 'preview')
