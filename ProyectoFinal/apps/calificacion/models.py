from django.db import models
from django.core.validators import MaxValueValidator, MinValueValidator

class Calificacion(models.Model):
    calificacion_num = models.PositiveIntegerField(
        default=5,
        validators=[
            MinValueValidator(1),
            MaxValueValidator(5)
        ],
        help_text="Puntuación de 1 a 5 estrellas"
    )
    autor = models.ForeignKey(
        'custom_user.CustomUser', 
        on_delete=models.CASCADE, 
        related_name='calificacion_autor_id',
        null=True # Permitir nulos temporalmente
    )  
    curso = models.ForeignKey(
        'cursada.Cursada', 
        on_delete=models.CASCADE, 
        related_name='calificacion_curso',
        null=True,
        default=None
    )
    fecha = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ['-fecha']

    def __str__(self):
        return f'Calificación de {self.autor_id}'
    
    def save(self, *args, **kwargs):
        super().save(*args, **kwargs)


