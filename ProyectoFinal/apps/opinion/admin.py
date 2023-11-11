from django.contrib import admin
from apps.opinion.models import Opinion

@admin.register(Opinion)
class OpinionAdmin(admin.ModelAdmin):
    list_display = ("descripcion", "get_id_usuario", "get_id_cursada", "fecha")

    def get_id_usuario(self, obj):
        return obj.fk_id_usuario.id

    def get_id_cursada(self, obj):
        return obj.fk_id_cursada.id if obj.fk_id_cursada else None

    get_id_usuario.short_description = "ID Usuario"
    get_id_cursada.short_description = "ID Cursada"


