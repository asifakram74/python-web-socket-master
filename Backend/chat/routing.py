from django.urls import path
from .consumers import ChatConsumer

# Define the WebSocket URL patterns for the chat application
websocket_urlpatterns = [
    # Route WebSocket connections at 'ws/chat/' to the ChatConsumer
    path('ws/chat/', ChatConsumer.as_asgi()),
]
