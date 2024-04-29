from django.db import models
from django.contrib.contenttypes.fields import GenericForeignKey
from django.contrib.contenttypes.models import ContentType
from django.utils import timezone
from apps.calificacion.models import Calificacion
# Esta estructura te brinda la flexibilidad de registrar opiniones sobre varias entidades y vincularlas a usuarios.


class Opinion(models.Model):
    titulo = models.CharField(max_length=200, default=None)
    contenido = models.TextField(default=None)  # Comentario de la opinión
    autor = models.ForeignKey('custom_user.CustomUser', on_delete=models.CASCADE, related_name='opiniones_usuario', default=None)  # Usuario que realizó la opinión
    curso= models.ForeignKey('cursada.Cursada', on_delete=models.CASCADE, related_name='opiniones_cursadas', default=None)
    fecha = models.DateTimeField(auto_now_add=True)  # Fecha de la opinión
    calificacion = models.ForeignKey(Calificacion, on_delete=models.CASCADE, related_name='opiniones_calificacion', default=None)  # Calificación de la opinión

    # Campos para la relación genérica
    content_type = models.ForeignKey(ContentType, on_delete=models.CASCADE, null=True)
    object_id = models.PositiveIntegerField(null=True)
    content_object = GenericForeignKey('content_type', 'object_id')

    def __str__(self):
        return f'Opinión de {self.autor}'


    def crear_opinion(self):
        # Este método es un poco redundante en Django, porque crear una instancia ya es "crear"
        self.save()

    def eliminar_opinion(self):
        # Este método ayudaría a eliminar la instancia del modelo de la base de datos
        self.delete()






    

    

   





