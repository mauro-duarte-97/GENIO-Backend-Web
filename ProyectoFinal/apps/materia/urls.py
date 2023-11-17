from django.urls import path
from apps.materia.views import MateriaDetailView
from .views import MateriaListView

urlpatterns = [
    path("detalle/<int:pk>", MateriaDetailView.as_view(), name="detalle_materia"),
    path("lista/", MateriaListView.as_view(), name="lista_materia"),]