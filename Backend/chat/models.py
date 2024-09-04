from django.db import models

class Message(models.Model):
    """
    Model representing a message in the chat application.

    Attributes:
        content (TextField): The text content of the message.
        timestamp (DateTimeField): The date and time when the message was created, 
                                   automatically set when the message is saved.
    """
    content = models.TextField()
    timestamp = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        """
        Returns a string representation of the message object.

        This method returns the first 50 characters of the message content, 
        which can be useful for displaying a summary in the Django admin interface 
        or in other places where the object is represented as a string.
        """
        return self.content[:50]
