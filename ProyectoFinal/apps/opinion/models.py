from django.db import models
from django.utils import timezone
from django.contrib.contenttypes.fields import GenericForeignKey
from django.contrib.contenttypes.models import ContentType
# Esta estructura te brinda la flexibilidad de registrar opiniones sobre varias entidades y vincularlas a usuarios.

class Puntaje(models.Model):
    # Aquí puedes agregar atributos para Puntaje, por ejemplo:
    valor = models.IntegerField(default=0)

class Opinion(models.Model):
    titulo = models.CharField(max_length=200)
    contenido = models.TextField()  # Comentario de la opinión
    autor = models.ForeignKey('custom_user.CustomUser', on_delete=models.CASCADE, related_name='opiniones_usuario', default=None)  # Usuario que realizó la opinión
    curso= models.ForeignKey('cursada.Cursada', on_delete=models.CASCADE, related_name='opiniones_cursadas', default=None)
    fecha = models.DateTimeField(auto_now_add=True)  # Fecha de la opinión
    puntaje = models.ForeignKey(Puntaje, on_delete=models.CASCADE)

    # Campos para la relación genérica
    content_type = models.ForeignKey(ContentType, on_delete=models.CASCADE)
    object_id = models.PositiveIntegerField()
    content_object = GenericForeignKey('content_type', 'object_id')

    def __str__(self):
        return f'Opinión de {self.usuario}'

    def crear_opinion(self):
        # Este método es un poco redundante en Django, porque crear una instancia ya es "crear"
        self.save()

    def eliminar_opinion(self):
        # Este método ayudaría a eliminar la instancia del modelo de la base de datos
        self.delete()






    

    

   





