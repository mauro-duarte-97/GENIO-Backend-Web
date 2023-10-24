from django.urls import path
from apps.carrera.views import CarreraTemplateView


urlpatterns = [
    path("", CarreraTemplateView.as_view(), name="carrera")]