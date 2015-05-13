from django.contrib import admin
from . import models


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
