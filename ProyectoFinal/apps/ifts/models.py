from django.db import models

class Institucion(models.Model):
    nombre = models.CharField(default="", max_length=50)
    #direccion = models.CharField(default="", max_length=50)
    