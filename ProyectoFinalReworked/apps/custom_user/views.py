from django.contrib.auth import authenticate, login
from django.contrib.auth.views import LoginView, LogoutView
from django.views.generic.base import TemplateView
from .models import CustomUser
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from .forms import RegistrationForm, CustomUserUpdateForm, CustomUserDeleteForm
from django.shortcuts import redirect, render
from django.http import HttpResponse
from django.http import HttpResponseBadRequest
from django.contrib import messages



class RegisterUsuarioView(CreateView):
    model = CustomUser
    form_class = RegistrationForm
    template_name = "index.html"
    success_url = "/"

    def form_valid(self, form):
        # Procesar el formulario si es válido
        user = form.save(commit=False)
        user.save()
        return super().form_valid(form)

    def form_invalid(self, form):
        # Agregar mensajes de error a la lista de mensajes
        for field, errors in form.errors.items():
            for error in errors:
                messages.error(self.request, f"{field}: {error}")
        return super().form_invalid(form)


class CustomLoginView(LoginView):
    template_name = "index.html"

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


class UserHomeView(TemplateView):
    template_name = "userHome.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        return context


class CustomProfileView(TemplateView):
    model = CustomUser
    template_name = "perfil.html"  # Nombre del template
    context_object_name = "usuario"  # Nombre del objeto en el contexto

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        user_id = self.kwargs.get("pk")
        user = CustomUser.objects.get(pk=user_id)
        context["usuario"] = user
        return context


class EditarUsuarioView(UpdateView):
    model = CustomUser
    form_class = CustomUserUpdateForm
    template_name = "editar_usuario.html"
    success_url = "perfil_usuario/"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        user_id = self.kwargs.get("pk")
        user = CustomUser.objects.get(pk=user_id)
        context["usuario"] = user
        return context

        # def post(self, request, *args, **kwargs):
        # # Obtener el usuario actual
        # user = self.request.user
        # # Obtener la contraseña actual ingresada por el usuario
        # old_password = request.POST.get("old-password")
        # # Verificar la contraseña actual
        # user = authenticate(request, email=user.email, password=old_password)
        # # Si la autenticación es exitosa, proceder con la actualización del usuario
        # if user is not None:
        #     # Obtener la nueva contraseña ingresada por el usuario
        #     new_password = request.POST.get("new-password")
        #     # Obtener el formulario y actualizar la contraseña
        #     form = self.get_form()
        #     if form.is_valid():
        #         # Guardar la nueva contraseña en el modelo de usuario
        #         user.set_password(new_password)
        #         user.save()
        #         # Mensaje de éxito
        #         messages.success(request, "Contraseña cambiada correctamente.")
        #     else:
        #         # Si el formulario no es válido, mostrar errores
        #         return self.form_invalid(form)
        # else:
        #     # Si la autenticación falla, mostrar un mensaje de error
        #     messages.error(request, "La contraseña actual es incorrecta.")
        # # Redirigir a la página de perfil del usuario
        # return redirect("perfil_usuario", pk=user.pk)


class EliminarUsuarioView(DeleteView):
    model = CustomUser
    form_class = CustomUserDeleteForm
    template_name = "eliminar_usuario.html"
    success_url = "/"


def google_auth(request):
    # Aquí deberías manejar la lógica de autenticación de Google
    # Esto puede implicar redirigir al usuario a la URL de autenticación de Google y luego procesar el token devuelto por Google.
    # Aquí solo redirigimos al usuario a la página de inicio por ahora.
    return redirect(
        "userHome"
    )  # Cambia 'inicio' por el nombre de la URL de tu página de inicio



# class CustomLoginView(LoginView):
#     template_name = (
#         "index.html"  # Especifica el nombre del template de inicio de sesión
#     )

#     def post(self, request, *args, **kwargs):
#         # Obtener los datos de usuario del formulario de inicio de sesión
#         email = request.POST.get("email")
#         password = request.POST.get("password")

#         # Autenticar al usuario utilizando la función authenticate de Django
#         user = authenticate(request, email=email, password=password)

#         if user is not None:
#             # Si el usuario es autenticado correctamente, iniciar sesión y redirigir
#             login(request, user)
#             return redirect("user_home")
#         else:
#             # Si la autenticación falla, mostrar un mensaje de error en el mismo formulario de inicio de sesión
#             return render(
#                 request,
#                 self.template_name,
#                 {"error_message": "Usuario o contraseña incorrectos"},
# )
