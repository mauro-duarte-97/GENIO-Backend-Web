from django.contrib import admin
from apps.materia.models import Materia

@admin.register(Materia)
class MateriaAdmin(admin.ModelAdmin):
    list_display = ("nombre", "get_id_carrera", "dificultad")

    def get_id_carrera(self, obj):
        return obj.fk_id_carrera.id

    def dificultad(self, obj):
        votaciones = obj.votaciones.all()
        if votaciones:
            return sum(voto.valor for voto in votaciones) / len(votaciones)

    get_id_carrera.short_description = "ID Carrera"
    dificultad.short_description = "Dificultad"
