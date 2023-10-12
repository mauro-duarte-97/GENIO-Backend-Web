from django.db import models

# Permite que los usuarios dejen opiniones sin necesidad de especificar una entidad específica si no lo desean.

# Esta estructura te brinda la flexibilidad de registrar opiniones sobre varias entidades y vincularlas a usuarios.


class Opinion(models.Model):
    usuario = models.ForeignKey('custom_user.CustomUser', on_delete=models.CASCADE)  # Usuario que realizó la opinión
    institucion = models.ForeignKey('ifts.Institucion', on_delete=models.CASCADE, null=True, blank=True)
    #carrera = models.ForeignKey('carrera.Carrera', on_delete=models.CASCADE, null=True, blank=True)
    #materia = models.ForeignKey('materia.Materia', on_delete=models.CASCADE, null=True, blank=True)
    #profesor = models.ForeignKey('profesor.Profesor', on_delete=models.CASCADE, null=True, blank=True)
    comentario = models.TextField()  # Comentario de la opinión
    fecha = models.DateTimeField(auto_now_add=True)  # Fecha de la opinión

    def __str__(self):
        return f'Opinión de {self.usuario}'








