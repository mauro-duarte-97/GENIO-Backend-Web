from django.contrib import admin
from apps.institucion.models import Institucion

@admin.register(Institucion)
class institucionAdmin(admin.ModelAdmin):
    list_display = ("nombre","carrera","ubicacion",)

