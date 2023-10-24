from django.urls import path
from apps.custom_user.views import CustomUserTemplateView


urlpatterns = [
    path("", CustomUserTemplateView.as_view(), name="custom_user")]