from django.urls import path
from .views import CustomLoginView, RegisterUsuarioView, CustomLogoutView, GoogleAuthView
# from django.contrib.auth import views as auth_views
# from .views import google_auth

urlpatterns = [
    path("", CustomLoginView.as_view(), name="index"),
    path('register/', RegisterUsuarioView.as_view(), name='registrar_usuario'),
    path("login/", CustomLoginView.as_view(), name="login"),
    path("", CustomLogoutView.as_view(), name="logout"),
    path('google/', GoogleAuthView.as_view(), name='google-auth'),
    # path('cambiar-contraseña/', auth_views.PasswordChangeView.as_view(), name='cambiar_contraseña'),
    
    # path('google-auth/', google_auth, name='google-auth'),
]