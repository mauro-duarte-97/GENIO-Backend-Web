from django.shortcuts import render
from django.views.generic import TemplateView


class ProfesorTemplateView(TemplateView):
    template_name = "profesor_home.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        return context
