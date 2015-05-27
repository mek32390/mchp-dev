from django.contrib import admin
from . import models


class StudyGuideCampaignSubscribersInline(admin.TabularInline):
    model = models.StudyGuideCampaignSubscriber
    extra = 0
    fields = ('user', 'uuid', 'notified', 'opened', 'clicked', 'unsubscribed')
    ordering = ('user__username',)


@admin.register(models.StudyGuideCampaignSubscriber)
class StudyGuideCampaignSubscriberAdmin(admin.ModelAdmin):
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


@admin.register(models.StudyGuideCampaign)
class StudyGuideCampaignAdmin(admin.ModelAdmin):
    list_display = ('name', 'template', 'active', 'when', 'until')
    fieldsets = (
        (None, {
            'fields': ['name', 'subject', 'template',
                       'sender_name', 'sender_address'],
        }),
        ('Important dates', {
            'fields': ['when', 'until'],
        }),
    )
    readonly_fields = ('sender_name', 'sender_address')
    inlines = [StudyGuideCampaignSubscribersInline]


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
