from django.db import models

class DetalleCalificacion(models.Model):
    tipo_calificacion = models.CharField(default="", max_length=50)  # Usuario que realizó la opinión
    id_calificacion = models.CharField(default="", max_length=3)
