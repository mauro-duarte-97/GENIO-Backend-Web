from django.db import models

class DetalleCalificacion(models.Model):
    PROFESOR = 'Profesor'
    INSTITUCION = 'Institución'
    CARRERA = 'Carrera'
    MATERIA = 'Materia'

    TIPO_CALIFICACION_CHOICES = [(PROFESOR, 'Profesor'),(INSTITUCION, 'Institución'),(CARRERA, 'Carrera'),(MATERIA, 'Materia'),]

    fk_id_calificacion = models.ForeignKey('calificacion.Calificacion', on_delete=models.CASCADE, default=None)
    tipo_calificacion = models.CharField(max_length=50, choices=TIPO_CALIFICACION_CHOICES, default=INSTITUCION, blank=True, null=True)

    def __str__(self):
        return self.tipo_calificacion

