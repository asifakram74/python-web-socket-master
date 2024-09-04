from django.shortcuts import render
from rest_framework import generics

from .models import Message
from .serializers import MessageSerializer

# Function-based view for rendering the home page of the chat application
def home(request):
    """
    Renders the home.html template for the chat application.

    Args:
        request: The HTTP request object.

    Returns:
        HttpResponse: The rendered home.html template.
    """
    return render(request, 'chat/home.html')


# Class-based view for handling the list and creation of Message objects via REST API
class MessageListCreateAPIView(generics.ListCreateAPIView):
    """
    API view for listing all messages and creating a new message.

    Inherits from DRF's ListCreateAPIView to provide GET and POST methods for
    retrieving and creating messages.

    Attributes:
        queryset: The queryset of Message objects to be retrieved or created.
        serializer_class: The serializer class used to serialize and deserialize Message objects.
    """
    queryset = Message.objects.all()  # Retrieve all Message objects
    serializer_class = MessageSerializer  # Use MessageSerializer for serialization
