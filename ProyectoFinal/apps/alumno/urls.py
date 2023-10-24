from django.urls import path
from apps.alumno.views import AlumnoTemplateView


urlpatterns = [
    path("", AlumnoTemplateView.as_view(), name="alumno")]