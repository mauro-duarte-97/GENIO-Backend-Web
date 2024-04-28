from django.urls import path
from apps.profesor.views import ProfesorDetailView
from apps.opinion.views import OpinionListView # Importa la vista de opiniones

urlpatterns = [
    path("detalle/<int:pk>", ProfesorDetailView.as_view(), name="detalle_profesor"),
    path('<int:entity_id>/opinion_historica/', OpinionListView.as_view(), kwargs={'model_name': 'profesor'}, name='opiniones_profesor'),

]