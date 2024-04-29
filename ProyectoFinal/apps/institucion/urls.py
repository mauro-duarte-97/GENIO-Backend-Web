from django.urls import path
from apps.institucion.views import InstitucionTemplateView, InstitucionListView # Importa las vistas de instituciones
from apps.opinion.views import OpinionListView # Importa la vista de opiniones



urlpatterns = [
    path("detalle/", InstitucionTemplateView.as_view(), name="detalle_institucion"),
    path("lista/", InstitucionListView.as_view(), name="lista_instituciones"),
    path('<int:institucion_id>/opiniones/', OpinionListView.as_view(), name='opiniones_por_institucion'),
]

