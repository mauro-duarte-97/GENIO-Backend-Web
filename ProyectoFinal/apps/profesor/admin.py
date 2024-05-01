from django.contrib import admin
from apps.profesor.models import Profesor

@admin.register(Profesor)
class ProfesorAdmin(admin.ModelAdmin):
    list_display = ("nombre", "get_usuario_id", "get_materia_id", "img_perfil")

    def get_usuario_id(self, obj):
        return obj.usuario.id

    def get_materia_id(self, obj):
        return obj.materia.id

    get_usuario_id.short_description = "ID Usuario"
    get_materia_id.short_description = "ID Materia"

