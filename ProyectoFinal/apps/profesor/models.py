from django.db import models

class Profesor(models.Model):
    nombre = models.CharField(max_length=100, blank=True, null=True, default=None)
    usuario = models.ForeignKey('custom_user.CustomUser', on_delete=models.CASCADE, default=None)  # Usuario del profesor
    materia = models.ForeignKey('materia.Materia', on_delete=models.CASCADE, default=1)  # Id de la materia del profesor
    img_perfil = models.ImageField(upload_to='perfiles/profesores_uploads/', blank=True, null=True, default='perfiles/Profesores/ProfesorDefault.jpeg')

    def __str__(self):
        return self.nombre