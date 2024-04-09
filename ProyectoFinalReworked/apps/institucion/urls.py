from django.urls import path
from apps.institucion.views import InstitucionTemplateView
from .views import InstitucionListView

urlpatterns = [
    path("detalle/", InstitucionTemplateView.as_view(), name="detalle_institucion"),
    path("lista/", InstitucionListView.as_view(), name="lista_institucion"),]

