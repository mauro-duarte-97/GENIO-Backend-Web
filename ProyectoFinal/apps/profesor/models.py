from django.db import models

class Profesor(models.Model):
    nombre = models.CharField(max_length=100, blank=True, null=True, default=None)
    fk_id_usuario = models.ForeignKey('custom_user.CustomUser', on_delete=models.CASCADE, default=None)  # Usuario que realizó la opinión
    

    def __str__(self):
        return self.nombre