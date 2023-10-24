from django.contrib import admin
from apps.alumno.models import Alumno

@admin.register(Alumno)
class alumnoAdmin(admin.ModelAdmin):
    list_display = ("nombre","calificacion","opinion", "cursada",)
