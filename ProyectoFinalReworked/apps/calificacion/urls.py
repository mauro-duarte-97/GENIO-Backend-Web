from django.urls import path
from apps.calificacion.views import CalificacionTemplateView


urlpatterns = [
    path("", CalificacionTemplateView.as_view(), name="calificacion")]