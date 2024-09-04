from django.urls import path
from .views import home, MessageListCreateAPIView

# Define the URL patterns for the chat application
urlpatterns = [
    # URL pattern for the home page, which renders the chat interface
    path('', home, name='home'),

    # URL pattern for the Message API, which allows listing and creating messages
    path('api/messages/', MessageListCreateAPIView.as_view(), name='message-list-create'),
]
