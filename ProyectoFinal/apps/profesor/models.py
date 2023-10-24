from django.db import models

class Profesor(models.Model):
    nombre = models.CharField(max_length=100)
    cursada = models.ForeignKey('cursada.Cursada', on_delete=models.CASCADE, related_name='profesor_cursada')
    calificacion = models.DecimalField(max_digits=3, decimal_places=2)
    # experiencia = models.PositiveIntegerField()
    # opinion = models.TextField(null=True, blank=True)
    # disponibilidad = models.CharField(max_length=100, null=True, blank=True)
    
    # Otras relaciones y campos según tus necesidades

    def __str__(self):
        return self.nombre