from django.urls import path
from .views import CustomLoginView, RegisterUsuarioView
# from .views import google_auth

urlpatterns = [
    path("", CustomLoginView.as_view(), name="index"),
    path('register/', RegisterUsuarioView.as_view(), name='registrar_usuario'),
    path("login/", CustomLoginView.as_view(), name="login"),
    # path('google-auth/', google_auth, name='google-auth'),
]