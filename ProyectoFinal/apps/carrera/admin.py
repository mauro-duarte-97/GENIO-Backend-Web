from django.contrib import admin
from apps.carrera.models import Carrera

@admin.register(Carrera)
class carreraAdmin(admin.ModelAdmin):
    list_display = ("titulo","duracion", "fk_id_institucion",)

    def dificultad(self, obj):
        votaciones = obj.votaciones.all()
        if votaciones:
            return sum(voto.valor for voto in votaciones) / len(votaciones)