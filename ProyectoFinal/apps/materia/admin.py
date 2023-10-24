from django.contrib import admin
from apps.materia.models import Materia

@admin.register(Materia)
class materiaAdmin(admin.ModelAdmin):
    list_display = ("nombre","duracion","cursada",)

