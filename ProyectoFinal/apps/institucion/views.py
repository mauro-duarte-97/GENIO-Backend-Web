from django.shortcuts import render
from django.views.generic import TemplateView
from django.views.generic import ListView
from django.views.generic import DetailView
from .models import Institucion

class InstitucionTemplateView(TemplateView):
    template_name = "institucion_home.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        return context

class InstitucionListView(ListView):
    model = Institucion
    template_name = "lista_institucion.html"
    context_object_name = "objetos"

class InstitucionDetailView(DetailView):
    model = Institucion
    template_name = 'detalle_institucion.html'  # Nombre del template
    context_object_name = 'institucion'  # Nombre del objeto en el contexto

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['institucion_ubicacion'] = self.object.ubicacion
        return context
 