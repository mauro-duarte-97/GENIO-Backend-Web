from django.urls import path
from .views import CustomLoginView, CustomLogoutView, GuiaEstudianteHomeView

urlpatterns = [
    path("login/", CustomLoginView.as_view(), name="login"),
    path("logout/", CustomLogoutView.as_view(), name="logout"),
    path("guiaEstudiante/", GuiaEstudianteHomeView.as_view(), name="guiaEstudiante"),
]