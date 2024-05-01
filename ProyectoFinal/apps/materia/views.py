from django.shortcuts import render
from django.views.generic import ListView
from django.views.generic import DetailView
from .models import Materia


class MateriaListView(ListView):
    model = Materia
    template_name = "lista_materia.html"
    context_object_name = "materias"

class MateriaDetailView(DetailView):
    model = Materia
    template_name = 'detalle_materia.html'  # Nombre del template
    context_object_name = 'materia'  # Nombre del objeto en el contexto

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['titulo_carrera'] = self.object.fk_id_carrera.titulo
        return context
