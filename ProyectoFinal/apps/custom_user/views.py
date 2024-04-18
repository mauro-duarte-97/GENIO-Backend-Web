from django.views.generic.base import TemplateView
from apps.custom_user.forms import CustomUserDeleteForm, CustomUserUpdateForm
from apps.custom_user.models import CustomUser
from django.views.generic.edit import UpdateView, DeleteView
from django.shortcuts import redirect, render
from django.contrib import messages
from django.urls import reverse_lazy



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

class EditarUsuarioView(UpdateView):
    model = CustomUser
    form_class = CustomUserUpdateForm
    template_name = 'editar_usuario.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        user_id = self.kwargs.get('pk')
        user = CustomUser.objects.get(pk=user_id)
        context['usuario'] = user
        return context
    
    def form_valid(self, form):
        # Procesar el formulario si es válido
        user = form.save(commit=False)
        user.save()
        # Agregar mensaje de éxito a la lista de mensajes
        messages.success(self.request, 'Usuario actualizado correctamente')
        return super().form_valid(form)

    def form_invalid(self, form):
        # Agregar mensajes de error a la lista de mensajes
        for field, errors in form.errors.items():
            for error in errors:
                messages.error(self.request, f"{field}: {error}")
        return super().form_invalid(form)
    
    def get_success_url(self):
        # Obtener el ID del usuario que se ha actualizado
        user_id = self.object.pk
        # Construir la URL del perfil del usuario usando reverse_lazy
        return reverse_lazy('perfil_usuario', kwargs={'pk': user_id})
    
class EliminarUsuarioView(DeleteView):
    model = CustomUser
    form_class = CustomUserDeleteForm
    template_name = 'eliminar_usuario.html'
    success_url = '/'


def google_auth(request):
    # Aquí deberías manejar la lógica de autenticación de Google
    # Esto puede implicar redirigir al usuario a la URL de autenticación de Google y luego procesar el token devuelto por Google.
    # Aquí solo redirigimos al usuario a la página de inicio por ahora.
    return redirect('userHome')  # Cambia 'inicio' por el nombre de la URL de tu página de inicio
