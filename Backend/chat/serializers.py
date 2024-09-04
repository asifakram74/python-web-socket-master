from rest_framework import serializers
from .models import Message

class MessageSerializer(serializers.ModelSerializer):
    """
    Serializer for the Message model.

    This serializer converts the Message model instances into JSON format
    and validates incoming data to create or update Message instances.
    """
    class Meta:
        model = Message  # Specifies the model to be serialized
        fields = ['id', 'content', 'timestamp']  # Specifies the fields to include in the serialized output
