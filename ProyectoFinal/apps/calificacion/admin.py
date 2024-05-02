from django.contrib import admin
from apps.calificacion.models import Calificacion

@admin.register(Calificacion)
class CalificacionAdmin(admin.ModelAdmin):
    list_display = ("calificacion_num", "get_autor_id", "get_curso", "fecha")

    def get_autor_id(self, obj):
        return obj.autor.id if obj.autor else "Sin Autor"

    def get_curso(self, obj):
        return obj.curso.id if obj.curso.id else None

    get_autor_id.short_description = "ID Usuario"
    get_curso.short_description = "ID Cursada"
