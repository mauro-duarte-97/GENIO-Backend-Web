from django.contrib.auth.mixins import LoginRequiredMixin
from django.shortcuts import render
from django.views.generic import TemplateView


class AlumnoTemplateView(LoginRequiredMixin, TemplateView):
    template_name = "alumno_home.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        return context
