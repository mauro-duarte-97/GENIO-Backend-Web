from django.contrib import admin
from apps.institucion.models import Institucion

@admin.register(Institucion)
class InstitucionAdmin(admin.ModelAdmin):
    list_display = ("nombre", "ubicacion", "get_id_usuario")

    def get_id_usuario(self, obj):
        return obj.fk_id_usuario.id

    get_id_usuario.short_description = "ID Usuario"
