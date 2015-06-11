# from django.contrib import admin
# from . import models


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


# class CampaignSubscribersInline(admin.TabularInline):
#     model = models.CampaignSubscriber
#     extra = 0
#     fields = ('user', 'uuid', 'notified', 'opened', 'clicked', 'unsubscribed')
#     ordering = ('user__username',)


# @admin.register(models.Campaign)
# class CampaignAdmin(admin.ModelAdmin):
#     list_display = ('name', 'template', 'active', 'when', 'until')
#     fieldsets = (
#         (None, {
#             'fields': ['name', 'sender_name', 'sender_address', 'template'],
#         }),
#         ('Important dates', {
#             'fields': ['when', 'until'],
#         }),
#     )
#     inlines = [CampaignSubscribersInline]
