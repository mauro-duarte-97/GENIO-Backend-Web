# Generated by Django 5.0.4 on 2024-04-29 07:38

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('carrera', '0004_alter_carrera_titulo'),
    ]

    operations = [
        migrations.AddField(
            model_name='carrera',
            name='img_perfil',
            field=models.ImageField(blank=True, default='perfiles/Carreras/Carreras-Perfil.jpeg', null=True, upload_to='perfiles/Carreras/'),
        ),
    ]
