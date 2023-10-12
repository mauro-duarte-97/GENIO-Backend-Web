from django.db import models

class Carrera(models.Model):
    titulo = models.CharField(default="", max_length=50)
    duracion = models.PositiveIntegerField()
    dificultad = models.CharField(default="", max_length=50)
    calificacion = models.DecimalField(max_digits=3, decimal_places=2)
    opinion = models.ForeignKey('opinion.Opinion.opinionCarrera', on_delete=models.CASCADE)