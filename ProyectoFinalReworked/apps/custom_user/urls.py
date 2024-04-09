from django.urls import path
from .views import (
    CustomLoginView,
    CustomLogoutView,
    CustomProfileView,
    RegisterUsuarioView,
    EditarUsuarioView,
    EliminarUsuarioView,
    UserHomeView,
)  # , HomeView
from .views import google_auth

urlpatterns = [
    # path("login/", CustomLoginView.as_view(), name="login"),
    # path("", CustomLogoutView.as_view(), name="logout"),
    # path("", HomeView.as_view(), name="index"),
    path("", CustomLoginView.as_view(), name="index"),
    path("register/", RegisterUsuarioView.as_view(), name="registrar_usuario"),
    path("login/", CustomLoginView.as_view(), name="login"),
    path("userHome/", UserHomeView.as_view(), name="user_home"),
    path("perfil/<int:pk>/", CustomProfileView.as_view(), name="perfil_usuario"),
    path("editar/<int:pk>/", EditarUsuarioView.as_view(), name="editar_usuario"),
    path("eliminar/<int:pk>/", EliminarUsuarioView.as_view(), name="eliminar_usuario"),
    path("google-auth/", google_auth, name="google-auth"),
]
