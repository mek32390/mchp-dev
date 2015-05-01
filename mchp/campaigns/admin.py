from django.contrib import admin
from .models import CampaignMailer


@admin.register(CampaignMailer)
class CampaignMailerAdmin(admin.ModelAdmin):
    fieldsets = (
        (None, {
            'fields': ['title', 'active'],
        }),
        ('Content', {
            'fields': ['subject', 'body'],
        }),
    )
