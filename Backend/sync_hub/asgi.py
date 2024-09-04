"""
ASGI config for sync_hub project.

This module sets up the ASGI application for the Django project. It configures the 
ASGI callable that handles both HTTP and WebSocket connections. The application 
is composed of Django's ASGI application for HTTP and Channels for WebSocket 
handling.

For more information on this file, see
https://docs.djangoproject.com/en/5.0/howto/deployment/asgi/
"""

import os
from django.core.asgi import get_asgi_application

# Setting up the environment variable for Django settings
print("Setting up DJANGO_SETTINGS_MODULE")
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'sync_hub.settings')

try:
    # Load Django's ASGI application
    django_asgi_app = get_asgi_application()
    print("Django ASGI application loaded successfully")
except Exception as e:
    # Handle errors in loading the Django ASGI application
    print(f"Error while loading ASGI application: {e}")
    raise e

print("Importing Channels components")
from channels.routing import ProtocolTypeRouter, URLRouter
from channels.auth import AuthMiddlewareStack
from chat.routing import websocket_urlpatterns

# Define the ASGI application to handle different types of connections
application = ProtocolTypeRouter({
    "http": django_asgi_app,  # Use Django's ASGI application to handle HTTP requests
    "websocket": AuthMiddlewareStack(
        URLRouter(
            websocket_urlpatterns  # Route WebSocket connections to the appropriate consumer
        )
    ),
})

print("ASGI application setup complete")
