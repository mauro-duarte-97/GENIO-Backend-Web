from django.shortcuts import render
from django.views.generic import ListView
from django.views.generic import DetailView
from .models import Profesor

class ProfesorListView(ListView):
    model = Profesor
    template_name = "lista_profesor.html"
    context_object_name = "profesores"

class ProfesorDetailView(DetailView):
    model = Profesor
    template_name = 'detalle_profesor.html'  # Nombre del template
    context_object_name = 'profesor'  # Nombre del objeto en el contexto

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['nombre_institucion'] = self.object.id_institucion.nombre
        return context
