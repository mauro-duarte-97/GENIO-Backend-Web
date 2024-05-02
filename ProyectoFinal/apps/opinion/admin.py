from django.contrib import admin
from apps.opinion.models import Opinion

@admin.register(Opinion)
class OpinionAdmin(admin.ModelAdmin):
    list_display = ("titulo", "contenido", "get_autor", "get_curso", "fecha", "calificacion")

    def get_autor(self, obj):
        return obj.autor.nombre if obj.autor.nombre else None

    def get_curso(self, obj):
        return obj.curso.id if obj.curso.id else None

    get_autor.short_description = "Name Usuario"
    get_curso.short_description = "ID Cursada"


