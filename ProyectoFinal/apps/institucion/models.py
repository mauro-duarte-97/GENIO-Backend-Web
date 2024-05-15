from django.db import models

class Institucion(models.Model):
    nombre = models.CharField(default="IFTS", max_length=150, blank=True, null=True)
    ubicacion = models.CharField(default="Argentina", max_length=250, blank=True, null=True)
    url = models.CharField(default="", max_length=250, blank=True, null=True)
    usuario = models.ForeignKey('custom_user.CustomUser', on_delete=models.CASCADE, related_name='instituciones_usuario', default=None)
    img_perfil = models.ImageField(upload_to='ifts_uploads/', default='IFTS/IFTS18-FRONT.jpg' , blank=True, null=True)
    
    def __str__(self):
        return self.nombre