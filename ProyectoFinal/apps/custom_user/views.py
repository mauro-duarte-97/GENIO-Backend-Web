from django.contrib.auth.views import LoginView, LogoutView
from django.contrib import messages
from django.views.generic.base import TemplateView
from .models import CustomUser
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from .forms import CustomUserCreateForm, CustomUserUpdateForm, CustomUserDeleteForm
from django.urls import reverse_lazy


class CustomLoginView(LoginView):
    template_name = "login.html"

    def form_invalid(self, form):
        messages.error(
            self.request, "Credenciales incorrectas. Por favor, inténtalo de nuevo."
        )  # Mensaje de error
        return super().form_invalid(form)

class CustomLogoutView(LogoutView):
    pass

class HomeView(TemplateView):
    template_name = "home.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        return context
    
class CustomProfileView(TemplateView):
    model = CustomUser 
    template_name = 'perfil.html'  # Nombre del template
    context_object_name = 'usuario'  # Nombre del objeto en el contexto

class CrearUsuarioView(CreateView):
    model = CustomUser
    form_class = CustomUserCreateForm
    template_name = 'crear_usuario.html'
    success_url = '/perfil/'

class EditarUsuarioView(UpdateView):
    model = CustomUser
    form_class = CustomUserUpdateForm
    template_name = 'editar_usuario.html'
    success_url = '/perfil/'

class EliminarUsuarioView(DeleteView):
    model = CustomUser
    form_class = CustomUserDeleteForm
    template_name = 'eliminar_usuario.html'
    success_url = reverse_lazy('/home/')