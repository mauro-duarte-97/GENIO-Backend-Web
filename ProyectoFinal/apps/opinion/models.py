from django.db import models

# Permite que los usuarios dejen opiniones sin necesidad de especificar una entidad específica si no lo desean.

# Esta estructura te brinda la flexibilidad de registrar opiniones sobre varias entidades y vincularlas a usuarios.


class Opinion(models.Model):
    descripcion = models.TextField()  # Comentario de la opinión
    fk_id_usuario = models.ForeignKey('custom_user.CustomUser', on_delete=models.CASCADE, related_name='opiniones_usuario', default=None)  # Usuario que realizó la opinión
    fk_id_cursada= models.ForeignKey('cursada.Cursada', on_delete=models.CASCADE, related_name='opiniones_cursadas', default=None)
    fecha = models.DateTimeField(auto_now_add=True)  # Fecha de la opinión

    def __str__(self):
        return f'Opinión de {self.usuario}'








