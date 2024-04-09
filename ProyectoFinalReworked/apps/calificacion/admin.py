from django.contrib import admin
from apps.calificacion.models import Calificacion

@admin.register(Calificacion)
class CalificacionAdmin(admin.ModelAdmin):
    list_display = ("calificacion_num", "get_id_usuario", "get_id_cursada", "fecha")

    def get_id_usuario(self, obj):
        return obj.fk_id_usuario.id

    def get_id_cursada(self, obj):
        return obj.fk_id_cursada.id

    get_id_usuario.short_description = "ID Usuario"
    get_id_cursada.short_description = "ID Cursada"
