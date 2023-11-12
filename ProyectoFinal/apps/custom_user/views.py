from django.contrib.auth.views import LoginView, LogoutView
from django.contrib import messages
from django.views.generic.base import TemplateView


class CustomLoginView(LoginView):
    template_name = "login.html"

    def form_invalid(self, form):
        messages.error(
            self.request, "Credenciales incorrectas. Por favor, inténtalo de nuevo."
        )  # Mensaje de error
        return super().form_invalid(form)


class CustomLogoutView(LogoutView):
    pass

class GuiaEstudianteHomeView(TemplateView):
    template_name = "guiaEstudiante_home.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        return context