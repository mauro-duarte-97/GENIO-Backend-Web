from pyexpat.errors import messages
from django import forms
from .models import CustomUser
from django.contrib.auth.views import LoginView, LogoutView

from django.contrib.admin.widgets import FilteredSelectMultiple
from django.contrib.auth.models import User
from django.shortcuts import render, redirect
from django.contrib.auth.forms import UserCreationForm

class CustomUserForm(forms.ModelForm):
    class Meta:
        model = CustomUser
        fields = ['email', 'password']
        widgets = {
            'email': forms.TextInput(attrs={'placeholder': 'Correo electrónico'}),
            'password': forms.EmailInput(attrs={'placeholder': 'Contraseña'}),
        }
    
class CustomUserUpdateForm(forms.ModelForm):
    class Meta:
        model = CustomUser
        fields = ['nombre', 'email', 'img_perfil']
        widgets = {
            'nombre': forms.TextInput(attrs={'placeholder': 'Nombre del alumno'}),
            'email': forms.EmailInput(attrs={'placeholder': 'Correo electrónico'}),
            'img_perfil': forms.FileInput()
        }

class CustomUserDeleteForm(forms.ModelForm):
    class Meta:
        model = CustomUser
        fields = []  # No necesitas campos, ya que es un formulario para eliminar

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['confirmacion'] = forms.BooleanField(
            required=True,
            label='Confirmar eliminación',
            help_text='Marca esta casilla para confirmar que deseas eliminar este usuario.',
        )

class CustomUserLoginForm(forms.Form):
    class Meta:
        model = CustomUser
        fields = ['email', 'password']
        widgets = {
            'email': forms.EmailInput(attrs={'placeholder': 'Correo electrónico'}),
            'password': forms.PasswordInput(attrs={'placeholder': 'Contraseña'}),
        }

# Login
class CustomLoginView(LoginView):
    class Meta:
        model = CustomUser
        fields = ["email", "password"]
        widgets = {
            "email": forms.EmailInput(attrs={"placeholder": "Correo electrónico"}),
            "password": forms.PasswordInput(attrs={"placeholder": "Contraseña"}),
        }

# Logout con boton confirmar:
class CustomLogoutView(LogoutView):
    pass


class LogoutConfirmationView(LogoutView):
    template_name = "index.html"

    def get(self, request, *args, **kwargs):
        return render(request, self.template_name)

# REGISTER   
class RegistrationForm(UserCreationForm):
    email = forms.EmailField(
        max_length=254, help_text="Required. Inform a valid email address."
    )

    class Meta:
        model = CustomUser
        fields = ("email", "password1", "password2")


# class CustomUserCreateForm(forms.ModelForm):
    # class Meta:
    #     model = CustomUser
    #     fields = ['nombre', 'email', 'password', 'tipo_usuario']
    #     widgets = {
    #         'nombre': forms.TextInput(attrs={'placeholder': 'Nombre del alumno'}),
    #         'email': forms.EmailInput(attrs={'placeholder': 'Correo electrónico'}),
    #         'tipo_usuario': forms.Select(attrs={'placeholder': 'Tipo de usuario'}),
    #     }
