from django.contrib import admin
from . import models


# @admin.register(models.CampaignTemplate)
# class CampaignTemplateAdmin(admin.ModelAdmin):
#     list_display = ('name',)
#     fieldsets = (
#         (None, {
#             'fields': ['name'],
#         }),
#         ('Content', {
#             'fields': ['subject', 'body'],
#         }),
#         # ('Important dates', {
#         #     'fields': ['updated', 'created'],
#         # })
#     )
#     # readonly_fields = ('created', 'updated')

@admin.register(models.CampaignSubscriber)
class CampaignSubscriberAdmin(admin.ModelAdmin):
    list_display = ('user', 'campaign', 'notified', 'opened', 'clicked',
                    'unsubscribed', 'uuid')


class CampaignSubscribersInline(admin.TabularInline):
    model = models.CampaignSubscriber
    extra = 0
    fields = ('user', 'uuid', 'notified', 'opened', 'clicked', 'unsubscribed')
    ordering = ('user__username',)


@admin.register(models.Campaign)
class CampaignAdmin(admin.ModelAdmin):
    list_display = ('active', 'when', 'until')
    fieldsets = (
        (None, {
            'fields': ['sender_name', 'sender_address'],
        }),
        ('Important dates', {
            'fields': ['when', 'until'],
        }),
    )
    inlines = [CampaignSubscribersInline]
