from django.db import models

class Cursada(models.Model):
    nombreFecha = models.CharField(max_length=100)
    profesor = models.ForeignKey('profesor.Profesor', on_delete=models.CASCADE, related_name='cursadas_profesor')
    calificacion = models.ForeignKey('calificacion.Calificacion', on_delete=models.CASCADE, related_name='cursadas_calificacion')
    #opinion = models.TextField(null=True, blank=True)

    
    # Otras relaciones y campos según tus necesidades

    def __str__(self):
        return self.nombre
