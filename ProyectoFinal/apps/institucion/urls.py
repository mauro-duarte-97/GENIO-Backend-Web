from django.urls import path
from apps.institucion.views import InstitucionTemplateView


urlpatterns = [
    path("", InstitucionTemplateView.as_view(), name="institucion")]