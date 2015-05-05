from django.contrib import admin
from .models import Campaign, CampaignTemplate, CampaignBlast


@admin.register(CampaignTemplate)
class CampaignTemplateAdmin(admin.ModelAdmin):
    fieldsets = (
        (None, {
            'fields': ['name'],
        }),
        ('Content', {
            'fields': ['subject', 'body'],
        }),
    )


@admin.register(Campaign)
class CampaignAdmin(admin.ModelAdmin):
    list_display = ('template', 'active', 'when', 'until')
    fieldsets = (
        (None, {
            'fields': ['name', 'template'],
        }),
        ('Important dates', {
            'fields': ['when', 'until'],
        }),
    )

@admin.register(CampaignBlast)
class CampaignBlastAdmin(admin.ModelAdmin):
    pass
    # list_display = ('campaign')
    # fieldsets = (
    #     (None, {
    #         'fields': ['template', 'category'],
    #     }),
    #     ('Important dates', {
    #         'fields': ['when', 'until'],
    #     }),
    # )

# @admin.register(Campaign)
# class CampaignAdmin(admin.ModelAdmin):
#     pass
