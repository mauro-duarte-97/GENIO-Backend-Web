from django.shortcuts import render
from django.views.generic import TemplateView


class CalificacionTemplateView(TemplateView):
    template_name = "calificacion_home.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        return context