from django.db import models

# Permite que los usuarios dejen opiniones sin necesidad de especificar una entidad específica si no lo desean.

# Esta estructura te brinda la flexibilidad de registrar opiniones sobre varias entidades y vincularlas a usuarios.


class Opinion(models.Model):
    opinion = models.TextField()  # Comentario de la opinión
    usuario = models.ForeignKey('custom_user.CustomUser', on_delete=models.CASCADE)  # Usuario que realizó la opinión
    cursada= models.ForeignKey('cursada.Cursada', on_delete=models.CASCADE, blank=True)
    #fecha = models.DateTimeField(auto_now_add=True)  # Fecha de la opinión
    #carrera = models.ForeignKey('carrera.Carrera', on_delete=models.CASCADE, null=True, blank=True)
    #materia = models.ForeignKey('materia.Materia', on_delete=models.CASCADE, null=True, blank=True)
    #profesor = models.ForeignKey('profesor.Profesor', on_delete=models.CASCADE, null=True, blank=True)

    def __str__(self):
        return f'Opinión de {self.usuario}'








