import { Component, OnInit, OnDestroy } from '@angular/core';
import { CommonModule } from '@angular/common';
import { FormsModule } from '@angular/forms';
import { WebSocketService } from '../websocket.service';
import { Subscription } from 'rxjs';

/**
 * The ChatComponent handles the chat interface and logic for sending
 * and receiving messages through a WebSocket connection.
 */
@Component({
  selector: 'app-chat',  // The custom HTML tag for this component
  templateUrl: './chat.component.html',  // The HTML template associated with this component
  styleUrls: ['./chat.component.css'],  // The CSS styles associated with this component
  standalone: true,  // Indicates that this component is standalone and does not need a module
  imports: [CommonModule, FormsModule]  // Import necessary modules for this component
})
export class ChatComponent implements OnInit, OnDestroy {
  message: string = '';  // The message currently being typed by the user
  messages: { content: string, type: string }[] = [];  // Array to hold sent and received messages
  private messageSubscription: Subscription | null = null;  // Subscription for WebSocket messages

  /**
   * Constructs the ChatComponent and injects the WebSocketService.
   * @param websocketService - The service used to communicate with the WebSocket.
   */
  constructor(private websocketService: WebSocketService) {}

  /**
   * Initializes the component and subscribes to WebSocket messages.
   * This method is called once the component is initialized.
   */
  ngOnInit(): void {
    // Subscribe to WebSocket messages when the component is initialized
    this.messageSubscription = this.websocketService.onMessage().subscribe((msg: any) => {
      if (msg.content && msg.content.trim() !== '') {
        this.messages.push({ content: msg.content, type: 'received' });  // Add received message to messages array
      } else {
        console.warn('Received an empty content:', msg);
      }
    });
  }

  /**
   * Sends the message typed by the user and clears the input field.
   * The sent message is immediately added to the messages array.
   */
  sendMessage(): void {
    if (this.message.trim()) {
      this.messages.push({ content: this.message, type: 'sent' });  // Add sent message to messages array
      this.websocketService.sendMessage({ message: this.message });  // Send the message via WebSocket
      this.message = '';  // Clear the input field after sending
    }
  }

  /**
   * Unsubscribes from the WebSocket when the component is destroyed to prevent memory leaks.
   */
  ngOnDestroy(): void {
    if (this.messageSubscription) {
      this.messageSubscription.unsubscribe();  // Unsubscribe from WebSocket messages
    }
  }
}
