from django.contrib import admin
from apps.carrera.models import Carrera

@admin.register(Carrera)
class carreraAdmin(admin.ModelAdmin):
    list_display = ("titulo","duracion", "materia",)