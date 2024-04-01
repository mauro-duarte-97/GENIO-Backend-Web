from imaplib import _Authenticator
from django.contrib.auth import login
from django.contrib.auth.views import LoginView, LogoutView
from django.contrib import messages
from django.views.generic.base import TemplateView
from .models import CustomUser
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from .forms import CustomUserCreateForm, CustomUserUpdateForm, CustomUserDeleteForm
from django.urls import reverse_lazy
from django.shortcuts import redirect, render

class CustomLoginView(LoginView):
    template_name = "login.html"

    def form_valid(self, form):

        messages.success(self.request, "¡Bienvenido de nuevo!")
        return super().form_valid(form)
    
    def form_invalid(self, form):
        messages.error(
            self.request, "Credenciales incorrectas. Por favor, inténtalo de nuevo."
        )  # Mensaje de error
        return super().form_invalid(form)

class CustomLogoutView(LogoutView):
    template_name = "index.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        return context

class HomeView(TemplateView):
    template_name = "index.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        return context
    
class UserHomeView(TemplateView):
    template_name = "userHome.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        return context
    
class CustomProfileView(TemplateView):
    model = CustomUser 
    template_name = 'perfil.html'  # Nombre del template
    context_object_name = 'usuario'  # Nombre del objeto en el contexto

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        user_id = self.kwargs.get('pk')
        user = CustomUser.objects.get(pk=user_id)
        context['usuario'] = user
        return context

class CustomLoginView(LoginView):
    def get(self, request):
        return render(request, 'login.html')

    def post(self, request):
        email = request.POST.get('email')
        password = request.POST.get('password')
        user = _Authenticator(email=email, password=password)
        if user is not None:
            login(request, user)
            return redirect('home')
        else:
            return render(request, 'login.html', {'error_message': 'Usuario o contraseña incorrectos'})


class RegisterUsuarioView(CreateView):
    model = CustomUser
    form_class = CustomUserCreateForm
    template_name = 'registrar_usuario.html'
    success_url = 'perfil/'

class EditarUsuarioView(UpdateView):
    model = CustomUser
    form_class = CustomUserUpdateForm
    template_name = 'editar_usuario.html'
    success_url = 'perfil/'

class EliminarUsuarioView(DeleteView):
    model = CustomUser
    form_class = CustomUserDeleteForm
    template_name = 'eliminar_usuario.html'
    success_url = 'home/'



def google_auth(request):
    # Aquí deberías manejar la lógica de autenticación de Google
    # Esto puede implicar redirigir al usuario a la URL de autenticación de Google y luego procesar el token devuelto por Google.
    # Aquí solo redirigimos al usuario a la página de inicio por ahora.
    return redirect('userHome')  # Cambia 'inicio' por el nombre de la URL de tu página de inicio
