from django.views.generic import TemplateView
from django.views.generic import ListView
from django.views.generic import DetailView
from .models import Carrera

class CarreraTemplateView(TemplateView):
    template_name = "carrera_home.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        return context

class CarreraListView(ListView):
    model = Carrera
    template_name = "lista_carrera.html"
    context_object_name = "carreras"

class CarreraDetailView(DetailView):
    model = Carrera
    template_name = 'detalle_carrera.html'  # Nombre del template
    context_object_name = 'carrera'  # Nombre del objeto en el contexto

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['nombre_instituto'] = self.object.fk_id_institucion.nombre

        return context
