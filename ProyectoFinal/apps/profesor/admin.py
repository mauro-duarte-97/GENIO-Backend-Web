from django.contrib import admin
from apps.profesor.models import Profesor

@admin.register(Profesor)
class profesorAdmin(admin.ModelAdmin):
    list_display = ("nombre","cursada","calificacion",)

