from django.contrib import admin
from . import models


@admin.register(models.StudyGuideAnnouncement)
class StudyGuideAnnouncementAdmin(admin.ModelAdmin):
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


@admin.register(models.StudyGuideMetaCampaign)
class StudyGuideMetaCampaignAdmin(admin.ModelAdmin):
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
