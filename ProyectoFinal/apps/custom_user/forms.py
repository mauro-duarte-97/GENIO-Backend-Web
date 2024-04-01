from django import forms
from .models import CustomUser
from django.contrib.admin.widgets import FilteredSelectMultiple

class CustomUserForm(forms.ModelForm):
    class Meta:
        model = CustomUser
        fields = ['nombre', 'email']
        widgets = {
            'nombre': forms.TextInput(attrs={'placeholder': 'Nombre del alumno'}),
            'email': forms.EmailInput(attrs={'placeholder': 'Correo electrónico'}),
        }
    
class CustomUserCreateForm(forms.ModelForm):
    class Meta:
        model = CustomUser
        fields = ['nombre', 'email']
        widgets = {
            'nombre': forms.TextInput(attrs={'placeholder': 'Nombre del alumno'}),
            'email': forms.EmailInput(attrs={'placeholder': 'Correo electrónico'}),
        }

class CustomUserUpdateForm(forms.ModelForm):
    class Meta:
        model = CustomUser
        fields = ['nombre', 'email']
        widgets = {
            'nombre': forms.TextInput(attrs={'placeholder': 'Nombre del alumno'}),
            'email': forms.EmailInput(attrs={'placeholder': 'Correo electrónico'}),
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

class CustomUserLoginForm(forms.ModelForm):
    class Meta:
        model = CustomUser
        fields = ['email', 'password']
        widgets = {
            'email': forms.EmailInput(attrs={'placeholder': 'Correo electrónico'}),
            'password': forms.PasswordInput(attrs={'placeholder': 'Contraseña'}),
        }