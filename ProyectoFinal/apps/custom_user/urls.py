from django.urls import path
from .views import CustomProfileView, EditarUsuarioView, EliminarUsuarioView, UserHomeView 


urlpatterns = [
    path("userHome/", UserHomeView.as_view(), name="user_home"),
    path("perfil/<int:pk>/", CustomProfileView.as_view(), name="perfil_usuario"),
    path('editar/<int:pk>/', EditarUsuarioView.as_view(), name='editar_usuario'),
    path('eliminar/<int:pk>/', EliminarUsuarioView.as_view(), name='eliminar_usuario'),

]