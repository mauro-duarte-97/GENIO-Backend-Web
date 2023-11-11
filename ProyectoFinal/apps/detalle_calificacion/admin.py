from django.contrib import admin
from apps.detalle_calificacion.models import DetalleCalificacion

@admin.register(DetalleCalificacion)
class DetalleCalificacionAdmin(admin.ModelAdmin):
    list_display = ("tipo_calificacion", "get_id_calificacion",)

    def get_id_calificacion(self, obj):
        return obj.fk_id_calificacion.id

    get_id_calificacion.short_description = "ID Calificacion"
