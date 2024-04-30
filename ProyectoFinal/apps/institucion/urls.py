from django.urls import path
from apps.institucion.views import InstitucionListView # Imp


urlpatterns = [
    path("lista/", InstitucionListView.as_view(), name="lista_instituciones"),
]

