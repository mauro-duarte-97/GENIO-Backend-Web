from django.shortcuts import render
from django.views.generic import TemplateView
from django.views.generic import ListView
from .models import Institucion

class InstitucionTemplateView(TemplateView):
    template_name = "institucion_home.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        return context


class InstitucionListView(ListView):
    model = Institucion
    template_name = "institucion_list.html"
    context_object_name = "objetos"
