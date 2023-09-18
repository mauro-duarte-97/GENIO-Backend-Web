from django.db import models

class Calificacion(models.Model):
    nota = models.PositiveIntegerField()
