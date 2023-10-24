from django.contrib import admin
from apps.custom_user.models import CustomUser

@admin.register(CustomUser)
class custom_userAdmin(admin.ModelAdmin):
    list_display = ("nombre","tipo_usuario","registro",)
