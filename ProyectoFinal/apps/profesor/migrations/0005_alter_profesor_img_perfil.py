# Generated by Django 4.2.6 on 2024-05-15 17:21

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('profesor', '0004_profesor_img_perfil'),
    ]

    operations = [
        migrations.AlterField(
            model_name='profesor',
            name='img_perfil',
            field=models.ImageField(blank=True, default='Profesores/ProfesorDefault.jpeg', null=True, upload_to='profesores_uploads/'),
        ),
    ]
