from django.contrib import admin
from apps.profesor.models import Profesor

@admin.register(Profesor)
class ProfesorAdmin(admin.ModelAdmin):
    list_display = ("nombre", "get_id_usuario", "id_institucion",)

    def get_id_usuario(self, obj):
        return obj.fk_id_usuario.id

    get_id_usuario.short_description = "ID Usuario"

