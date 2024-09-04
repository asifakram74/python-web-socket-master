import { Injectable } from '@angular/core';
import { webSocket, WebSocketSubject } from 'rxjs/webSocket';

@Injectable({
  providedIn: 'root'
})
export class WebSocketService {
  private socket$: WebSocketSubject<any>;

  /**
   * Initializes a WebSocket connection to the specified URL
   * and subscribes to incoming messages, errors, and close events.
   */
  constructor() {
    // Establish a WebSocket connection to the specified endpoint
    this.socket$ = webSocket('ws://localhost:8000/ws/chat/');

    // Subscribe to incoming WebSocket messages, log errors, and handle connection closure
    this.socket$.subscribe(
      msg => console.log('Received message:', msg), // Log incoming messages
      err => console.error('WebSocket error:', err), // Log any errors
      () => console.log('WebSocket connection closed') // Log when the connection is closed
    );

    console.log('WebSocket connection established'); // Log the establishment of the WebSocket connection
  }

  /**
   * Sends a message through the WebSocket connection.
   * @param msg - The message object to be sent through the WebSocket.
   */
  sendMessage(msg: any): void {
    console.log('Sending message:', msg); // Log the message being sent
    this.socket$.next(msg); // Send the message through the WebSocket
  }

  /**
   * Returns an observable that emits messages received from the WebSocket.
   * This method allows components to subscribe to incoming WebSocket messages.
   * @returns An observable stream of incoming WebSocket messages.
   */
  onMessage() {
    return this.socket$.asObservable(); // Return an observable of the WebSocket messages
  }
}
