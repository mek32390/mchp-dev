from django.contrib import admin
from . import models


@admin.register(models.CampaignTemplate)
class CampaignTemplateAdmin(admin.ModelAdmin):
    list_display = ('name',)
    fieldsets = (
        (None, {
            'fields': ['name'],
        }),
        ('Content', {
            'fields': ['subject', 'body'],
        }),
        ('Important dates', {
            'fields': ['updated', 'created'],
        })
    )
    readonly_fields = ('created', 'updated')


class SubscribersInline(admin.TabularInline):
    model = models.Subscriber


@admin.register(models.Campaign)
class CampaignAdmin(admin.ModelAdmin):
    list_display = ('name', 'template', 'active', 'when', 'until')
    fieldsets = (
        (None, {
            'fields': ['name', 'template'],
        }),
        ('Important dates', {
            'fields': ['when', 'until', 'updated', 'created'],
        }),
    )
    readonly_fields = ('created', 'updated')
    inlines = [SubscribersInline]


@admin.register(models.CampaignBlast)
class CampaignBlastAdmin(admin.ModelAdmin):
    list_display = ('campaign', 'sent')
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
