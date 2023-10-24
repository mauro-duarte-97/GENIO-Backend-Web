from django.db import models

class CustomUser(models.Model):
    ALUMNO = 'Alumno'
    INSTITUCION = 'Institución'

    TIPO_USUARIO_CHOICES = [
        (ALUMNO, 'Alumno'),
        (INSTITUCION, 'Institución'),
    ]

    tipo_usuario = models.CharField(
        max_length=20,
        choices=TIPO_USUARIO_CHOICES,
        default=ALUMNO,  # Definir el valor por defecto
    )
    nombre = models.CharField(max_length=100)
    registro = models.CharField(max_length=100)
    # cursada = models.ForeignKey('cursada.Cursada', on_delete=models.CASCADE)
    # calificacion = models.DecimalField(max_digits=3, decimal_places=2)

    def __str__(self):
        return self.nombre
