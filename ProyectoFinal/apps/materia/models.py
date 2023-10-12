from django.db import models
import ifts

class Materia(models.Model):
    nombre = models.CharField(default="", max_length=50)
    duracion = models.CharField(default="", max_length=50)
    dificultad = models.CharField(default="", max_length=50)
    tipoCursada = models.CharField(default="", max_length=50)