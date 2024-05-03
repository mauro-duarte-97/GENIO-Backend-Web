from django.urls import path
from apps.profesor.views import ProfesorDetailView, ProfesorListView # Importa las vistas de profesores
from apps.opinion.views import OpinionListView # Importa la vista de opiniones

urlpatterns = [
    path("detalle/<int:pk>", ProfesorDetailView.as_view(), name="detalle_profesor"),
    path("lista/", ProfesorListView.as_view(), name="lista_profesores"),
]