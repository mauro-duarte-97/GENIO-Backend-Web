from django.db import models


class Materia(models.Model):
    nombre = models.CharField(default="", max_length=50)
    duracion = models.CharField(default="", max_length=50)
    cursada = models.ForeignKey('cursada.Cursada', on_delete=models.CASCADE)
    #dificultad = models.CharField(default="", max_length=50)