from django.urls import path
from apps.profesor.views import ProfesorDetailView
from .views import ProfesorListView

urlpatterns = [
    path("detalle/<int:pk>", ProfesorDetailView.as_view(), name="detalle_profesor"),
    path("lista/", ProfesorListView.as_view(), name="lista_profesor"),]