from django.db import models

class Profesor(models.Model):
    nombre = models.CharField(max_length=100, blank=True, null=True, default=None)
    fk_id_usuario = models.ForeignKey('custom_user.CustomUser', on_delete=models.CASCADE, default=None)  # Usuario del profesor
    id_institucion = models.ForeignKey('institucion.Institucion', on_delete=models.CASCADE, default=1)  # Id del institucion del profesor

    def __str__(self):
        return self.nombre