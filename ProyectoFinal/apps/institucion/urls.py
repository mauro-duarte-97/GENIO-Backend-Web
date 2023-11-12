from django.urls import path
from apps.institucion.views import InstitucionTemplateView
from .views import InstitucionListView

urlpatterns = [
    path("home/", InstitucionTemplateView.as_view(), name="institucion"),
    path("listaInstituciones/", InstitucionListView.as_view(), name="institucion_list"),]

