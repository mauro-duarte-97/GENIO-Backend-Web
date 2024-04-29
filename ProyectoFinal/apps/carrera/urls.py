from django.urls import path
from apps.carrera.views import CarreraDetailView, CarreraListView # Importa las vistas de carreras
from apps.opinion.views import OpinionListView # Importa la vista de opiniones

urlpatterns = [
    path("detalle/<int:pk>", CarreraDetailView.as_view(), name="detalle_carrera"),
    path("lista/", CarreraListView.as_view(), name="lista_carreras"),
    path("<int:entity_id>/opinion_historica/", OpinionListView.as_view(), kwargs={'model_name': 'carrera'}, name='opiniones_carrera'),
]