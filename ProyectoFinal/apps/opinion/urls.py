from django.urls import path
from apps.opinion.views import OpinionTemplateView


urlpatterns = [
    path("", OpinionTemplateView.as_view(), name="opinion")]