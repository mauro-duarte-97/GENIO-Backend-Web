from django.db import models

class Alumno(models.Model):
    nombre = models.CharField(max_length=100)
    cursada = models.ForeignKey('cursada.Cursada', on_delete=models.CASCADE)
    calificacion = models.DecimalField(max_digits=3, decimal_places=2)
    opinion = models.ForeignKey('opinion.Opinion', on_delete=models.CASCADE)
    # experiencia = models.PositiveIntegerField()
    # disponibilidad = models.CharField(max_length=100, null=True, blank=True)
    
    # Otras relaciones y campos según tus necesidades

    def __str__(self):
        return self.nombre
