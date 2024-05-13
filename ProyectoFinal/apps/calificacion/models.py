from django.db import models

class Calificacion(models.Model):

    calificacion_num = models.PositiveIntegerField(default=None)  # Puntuación de 1 a 5 estrellas
    fk_id_usuario = models.ForeignKey('custom_user.CustomUser', on_delete=models.CASCADE, related_name='calificacion', default=None)  # Usuario que realizó la calificación
    fk_id_cursada = models.ForeignKey('cursada.Cursada', on_delete=models.CASCADE, related_name='calificacion', default=None)
    fecha = models.DateTimeField(auto_now_add=True)  # Fecha de la calificación
    
    # Otros campos o atributos relacionados con la calificación, como comentario, etc.

    class Meta:
        ordering = ['-fecha']  # Para obtener las últimas 10 votaciones

    def __str__(self):
        return f'Calificación de {self.fk_id_usuario}'

    def save(self, *args, **kwargs):
        super().save(*args, **kwargs)
        # Lógica para calcular el promedio de calificación y la cantidad de estrellas

