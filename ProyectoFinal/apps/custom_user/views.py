from django.contrib.auth import authenticate,login
from django.contrib.auth.views import LoginView, LogoutView
from django.views.generic.base import TemplateView
from .models import CustomUser
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from .forms import CustomUserCreateForm, CustomUserUpdateForm, CustomUserDeleteForm
from django.shortcuts import redirect, render
from django.http import HttpResponse
from django.http import HttpResponseBadRequest

# # FUNCION INDEPENDIENTE PARA VER LOS DATOS DEL USUARIO EN EL PERFIL
# def mi_vista(request):
#     # Obtener el CustomUser correspondiente al usuario actualmente autenticado
#     custom_user = CustomUser.objects.get(id=request.user.id)
    
#     # Renderizar la plantilla 'perfil.html' y pasarle el objeto CustomUser como contexto
#     return render(request, 'perfil.html', {'custom_user': custom_user})

# # FUNCION INDEPENDIENTE PARA GUARDAR LA FOTO DE PERFIL
# def guardar_imagen(request):
#     if request.method == 'POST' and request.FILES.get('image'):
#         imagen = request.FILES['image']
#         # Aquí puedes procesar y guardar la imagen en el servidor
#         # Por ejemplo, guardarla en la carpeta de medios de Django
#         # o en un servicio de almacenamiento en la nube como AWS S3.
#         return HttpResponse('Imagen guardada correctamente.')
#     else:
#         return HttpResponseBadRequest('Se esperaba una solicitud POST con una imagen.')

# # FUNCION INDEPENDIENTE PARA REGISTRAR UN USUARIO
# def registro_usuario(request):
#     if request.method == 'POST':
#         form = CustomUserCreateForm(request.POST)
#         if form.is_valid():
#             # Guardar el nuevo usuario en la base de datos
#             form.save()
#             # Redirigir al usuario a una página de inicio de sesión, por ejemplo
#             return redirect('index')
#     else:
#         form = CustomUserCreateForm()
#     return render(request, 'registro_usuario.html', {'form': form})


class RegisterUsuarioView(CreateView):
    model = CustomUser
    form_class = CustomUserCreateForm
    template_name = 'registrar_usuario.html'
    success_url = '/'

class CustomLoginView(LoginView):
    template_name = 'index.html'  # Especifica el nombre del template de inicio de sesión

    def post(self, request, *args, **kwargs):
        # Obtener los datos de usuario del formulario de inicio de sesión
        email = request.POST.get('email')
        password = request.POST.get('password')

        # Autenticar al usuario utilizando la función authenticate de Django
        user = authenticate(request, email=email, password=password)

        if user is not None:
            # Si el usuario es autenticado correctamente, iniciar sesión y redirigir
            login(request, user)
            return redirect('user_home')
        else:
            # Si la autenticación falla, mostrar un mensaje de error en el mismo formulario de inicio de sesión
            return render(request, self.template_name, {'error_message': 'Usuario o contraseña incorrectos'})

class CustomLogoutView(LogoutView):
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

class EditarUsuarioView(UpdateView):
    model = CustomUser
    form_class = CustomUserUpdateForm
    template_name = 'editar_usuario.html'
    success_url = 'perfil_usuario/'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        user_id = self.kwargs.get('pk')
        user = CustomUser.objects.get(pk=user_id)
        context['usuario'] = user
        return context
    
    # def post(self, request, *args, **kwargs):
        # Obtener el usuario actual
        user = self.request.user
        # Obtener la contraseña actual ingresada por el usuario
        old_password = request.POST.get('old-password')
        # Verificar la contraseña actual
        user = authenticate(request, email=user.email, password=old_password)
        # Si la autenticación es exitosa, proceder con la actualización del usuario
        if user is not None:
            # Obtener la nueva contraseña ingresada por el usuario
            new_password = request.POST.get('new-password')
            # Obtener el formulario y actualizar la contraseña
            form = self.get_form()
            if form.is_valid():
                # Guardar la nueva contraseña en el modelo de usuario
                user.set_password(new_password)
                user.save()
                # Mensaje de éxito
                messages.success(request, 'Contraseña cambiada correctamente.')
            else:
                # Si el formulario no es válido, mostrar errores
                return self.form_invalid(form)
        else:
            # Si la autenticación falla, mostrar un mensaje de error
            messages.error(request, 'La contraseña actual es incorrecta.')
        # Redirigir a la página de perfil del usuario
        return redirect('perfil_usuario', pk=user.pk)

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
