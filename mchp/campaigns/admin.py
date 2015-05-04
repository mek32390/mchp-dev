from django.contrib import admin
from .models import CampaignTemplate, CampaignMailer


@admin.register(CampaignTemplate)
class CampaignTemplateAdmin(admin.ModelAdmin):
    fieldsets = (
        (None, {
            'fields': ['title'],
        }),
        ('Content', {
            'fields': ['subject', 'body'],
        }),
    )


@admin.register(CampaignMailer)
class CampaignMailerAdmin(admin.ModelAdmin):
    list_display = ('template', 'active', 'when', 'until', 'category')
    fieldsets = (
        (None, {
            'fields': ['template', 'category'],
        }),
        ('Important dates', {
            'fields': ['when', 'until'],
        }),
    )

# @admin.register(Campaign)
# class CampaignAdmin(admin.ModelAdmin):
#     pass
