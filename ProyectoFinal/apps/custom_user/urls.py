from django.urls import path
from .views import CustomLoginView, CustomLogoutView, HomeView, CustomProfileView, CrearUsuarioView, EditarUsuarioView, EliminarUsuarioView

urlpatterns = [
    path("login/", CustomLoginView.as_view(), name="login"),
    path("logout/", CustomLogoutView.as_view(), name="logout"),
    path("perfil/<int:pk>/", CustomProfileView.as_view(), name="perfil_usuario"),
    path("home/", HomeView.as_view(), name="home"),
    path('crear/', CrearUsuarioView.as_view(), name='crear_usuario'),
    path('editar/<int:pk>/', EditarUsuarioView.as_view(), name='editar_usuario'),
    path('eliminar/<int:pk>/', EliminarUsuarioView.as_view(), name='eliminar_usuario'),
]