from django.contrib import admin
from apps.detalle_calificacion.models import DetalleCalificacion

@admin.register(DetalleCalificacion)
class DetalleCalificacionAdmin(admin.ModelAdmin):
    list_display = ("tipo_calificacion","id_calificacion",)
