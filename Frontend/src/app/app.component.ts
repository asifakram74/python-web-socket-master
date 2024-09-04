import { Component } from '@angular/core';
import { RouterOutlet } from '@angular/router';
import { ChatComponent } from './chat/chat.component';

/**
 * The root component of the Angular application.
 * This component serves as the main container for the application,
 * housing the chat functionality and potentially other routed components.
 */
@Component({
  selector: 'app-root',  // The custom HTML tag for this component
  standalone: true,      // Indicates that this component is standalone and does not need a module
  imports: [RouterOutlet, ChatComponent],  // Imports required for routing and the chat feature
  templateUrl: './app.component.html',  // The HTML template associated with this component
  styleUrls: ['./app.component.css']    // The CSS styles associated with this component
})
export class AppComponent {
  title = 'sync_hub_frontend';  // The title property used within the component's template
}
