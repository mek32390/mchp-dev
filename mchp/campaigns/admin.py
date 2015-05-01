from django.contrib import admin
from .models import EventCampaignMailer


@admin.register(EventCampaignMailer)
class EventCampaignMailerAdmin(admin.ModelAdmin):
    fieldsets = (
        (None, {
            'fields': ['title', 'active'],
        }),
        ('Content', {
            'fields': ['subject', 'body'],
        }),
    )
