from django.db import models
from django.contrib.auth.models import User



class Calificacion(models.Model):

    calificacion = models.PositiveIntegerField()  # Puntuación de 1 a 5 estrellas
    usuario = models.ForeignKey('custom_user.CustomUser', on_delete=models.CASCADE)  # Usuario que realizó la calificación
    cursada = models.ForeignKey('cursada.Cursada', related_name='calificaciones', on_delete=models.CASCADE)
    fecha = models.DateTimeField(auto_now_add=True)  # Fecha de la calificación
    
    # Otros campos o atributos relacionados con la calificación, como comentario, etc.

    class Meta:
        ordering = ['-fecha']  # Para obtener las últimas 10 votaciones

    def __str__(self):
        return f'Calificación de {self.usuario} para {self.institucion}'

    def save(self, *args, **kwargs):
        super().save(*args, **kwargs)
        # Lógica para calcular el promedio de calificación y la cantidad de estrellas

