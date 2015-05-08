from django.contrib import admin
from . import models


@admin.register(models.CampaignTemplate)
class CampaignTemplateAdmin(admin.ModelAdmin):
    list_display = ('name',)
    fieldsets = (
        (None, {
            'fields': ['name', 'slug'],
        }),
        ('Content', {
            'fields': ['subject', 'body'],
        }),
        # ('Important dates', {
        #     'fields': ['updated', 'created'],
        # })
    )
    # readonly_fields = ('created', 'updated')


class CampaignSubscribersInline(admin.TabularInline):
    model = models.CampaignSubscriber
    extra = 1
    fields = ('user', 'notified', 'opens', 'clicks')
    # ordering = ('student__user__username',)  # [TODO]


@admin.register(models.Campaign)
class CampaignAdmin(admin.ModelAdmin):
    list_display = ('name', 'template', 'active', 'when', 'until')
    fieldsets = (
        (None, {
            'fields': ['name', 'template'],
        }),
        ('Important dates', {
            'fields': ['when', 'until'],
        }),
    )
    inlines = [CampaignSubscribersInline]


@admin.register(models.StudyGuideCampaignCoordinator)
class StudyGuideCampaignCoordinatorAdmin(admin.ModelAdmin):
    pass
    # list_display = ('name', 'template', 'active', 'when', 'until')
    # fieldsets = (
    #     (None, {
    #         'fields': ['name', 'template'],
    #     }),
    #     ('Important dates', {
    #         'fields': ['when', 'until'],
    #     }),
    # )
    # inlines = [CampaignSubscribersInline]
