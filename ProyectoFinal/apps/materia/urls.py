from django.urls import path
from apps.materia.views import MateriaTemplateView


urlpatterns = [
    path("", MateriaTemplateView.as_view(), name="materia")]