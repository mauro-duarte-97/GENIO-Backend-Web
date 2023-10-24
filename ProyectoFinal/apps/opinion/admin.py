from django.contrib import admin
from apps.opinion.models import Opinion

@admin.register(Opinion)
class opinionAdmin(admin.ModelAdmin):
    list_display = ("opinion","usuario","cursada",)

