from django.urls import path
from .views import FeedbackView, GmailView


urlpatterns = [path('', FeedbackView.as_view(), name='feedback'),
               path('gmail_api/', GmailView.as_view(), name='gmail_api')]
