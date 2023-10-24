from django.contrib import admin
from apps.cursada.models import Cursada

@admin.register(Cursada)
class cursadaAdmin(admin.ModelAdmin):
    list_display = ("nombreFecha","calificacion","profesor",)