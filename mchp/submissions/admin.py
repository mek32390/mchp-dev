from django.contrib import admin
from . import models


@admin.register(models.Syllabus)
class SyllabusAdmin(admin.ModelAdmin):
    pass


@admin.register(models.Roster)
class RosterAdmin(admin.ModelAdmin):
    pass


@admin.register(models.SyllabusReview)
class SyllabusReviewAdmin(admin.ModelAdmin):
    pass


@admin.register(models.RosterReview)
class RosterReviewAdmin(admin.ModelAdmin):
    pass
