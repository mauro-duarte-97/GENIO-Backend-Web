from django.urls import path
from apps.institucion.views import InstitucionTemplateView
from apps.opinion.views import OpinionListView # Importa la vista de opiniones
urlpatterns = [
    path("detalle/", InstitucionTemplateView.as_view(), name="detalle_institucion"),
    path('instituciones/<int:institucion_id>/opiniones/', OpinionListView.as_view(), name='opiniones_por_institucion'),
]

