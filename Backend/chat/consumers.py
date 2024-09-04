import json
from channels.generic.websocket import AsyncWebsocketConsumer
from asgiref.sync import sync_to_async

from .models import Message
from .serializers import MessageSerializer

class ChatConsumer(AsyncWebsocketConsumer):
    """
    WebSocket consumer that handles real-time communication for the chat application.

    This consumer handles WebSocket connections, receives and processes messages,
    saves them to the database, and sends back responses to the client.
    """

    async def connect(self):
        """
        Handles the event when a WebSocket connection is established.

        This method is called automatically when a client attempts to open a WebSocket connection.
        It accepts the connection, allowing further communication.
        """
        await self.accept()

    async def disconnect(self, close_code):
        """
        Handles the event when a WebSocket connection is closed.

        This method is called automatically when a client closes the WebSocket connection.
        Currently, it doesn't perform any specific action but can be extended as needed.

        Args:
            close_code (int): The WebSocket close code.
        """
        pass

    async def receive(self, text_data):
        """
        Handles incoming messages from the WebSocket.

        This method processes the received JSON message, saves it to the database,
        serializes it into a format matching the REST API, and sends it back to the client.

        Args:
            text_data (str): The JSON-formatted text data received from the WebSocket.
        """
        try:
            data = json.loads(text_data)
        except json.JSONDecodeError:
            # Send an error message if the JSON is invalid
            await self.send(text_data=json.dumps({
                'error': 'Invalid JSON format.'
            }))
            return

        message = data.get('message', '')

        # Save the message to the database
        message_instance = await self.save_message(message)

        # Serialize the message to match REST API format
        serialized_message = await self.serialize_message(message_instance)

        # Send the serialized message back through WebSocket
        await self.send(text_data=json.dumps(serialized_message))

    @sync_to_async
    def save_message(self, message):
        """
        Saves the received message to the database.

        This method is run asynchronously using Django's sync_to_async utility.

        Args:
            message (str): The content of the message to be saved.

        Returns:
            Message: The saved Message instance.
        """
        return Message.objects.create(content=message)

    @sync_to_async
    def serialize_message(self, message_instance):
        """
        Serializes a Message instance into a dictionary matching the REST API format.

        This method is run asynchronously using Django's sync_to_async utility.

        Args:
            message_instance (Message): The Message instance to serialize.

        Returns:
            dict: The serialized message data.
        """
        serializer = MessageSerializer(message_instance)
        return serializer.data
