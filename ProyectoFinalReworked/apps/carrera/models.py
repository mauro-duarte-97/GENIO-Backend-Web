from django.db import models

class Carrera(models.Model):
    titulo = models.CharField(default="Tecnicatura Superior", max_length=150, blank=True, null=True)
    duracion = models.PositiveIntegerField(default=None)
    fk_id_institucion = models.ForeignKey('institucion.Institucion', on_delete=models.CASCADE, related_name='carreras_institucion', default=None)
    
    def __str__(self):
        return self.titulo
    

class VotacionCarrera(models.Model):
    carrera = models.ForeignKey(Carrera, on_delete=models.CASCADE, default=None)
    usuario = models.ForeignKey('custom_user.CustomUser', on_delete=models.CASCADE, related_name='votaciones', default=None)
    valor = models.IntegerField(default=None)

    @property
    def dificultad(self):
        votaciones = VotacionCarrera.objects.all()
        if votaciones:
            return sum(voto.valor for voto in votaciones) / len(votaciones)
        else:
            return None
