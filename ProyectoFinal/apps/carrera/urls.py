from django.urls import path
from apps.carrera.views import CarreraDetailView
from .views import CarreraListView

urlpatterns = [
    path("detalle/<int:pk>", CarreraDetailView.as_view(), name="detalle_carrera"),
    path("lista/", CarreraListView.as_view(), name="lista_carrera"),]