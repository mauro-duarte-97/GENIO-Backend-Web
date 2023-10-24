from django.db import models

class Institucion(models.Model):
    nombre = models.CharField(default="", max_length=50)
    carrera = models.ForeignKey('carrera.Carrera', on_delete=models.CASCADE)
    ubicacion = models.CharField(default="", max_length=50)
    