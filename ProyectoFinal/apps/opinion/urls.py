# urls.py
from django.urls import path
from .views import OpinionListView, OpinionDetailView

urlpatterns = [
    path('<str:model_name>/<int:entity_id>/', OpinionListView.as_view(), name='opiniones_por_entidad'),
    path('<str:model_name>/<int:entity_id>/opinion/<int:pk>/detalle/', OpinionDetailView.as_view(), name='opinion_detalle'),
]
