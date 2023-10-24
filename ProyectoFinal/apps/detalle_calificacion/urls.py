from django.urls import path
from apps.detalle_calificacion.views import DetalleCalificacionTemplateView


urlpatterns = [
    path("", DetalleCalificacionTemplateView.as_view(), name="detalle_calificacion")]