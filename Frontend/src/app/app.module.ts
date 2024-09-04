import { BrowserModule } from '@angular/platform-browser';
import { NgModule } from '@angular/core';
import { FormsModule } from '@angular/forms';
import { AppComponent } from './app.component';
import { ChatComponent } from './chat/chat.component';

/**
 * The root module of the Angular application.
 * This module is responsible for bootstrapping the application
 * and declaring all components that are part of the application.
 */
@NgModule({
  declarations: [
    // Declare all components, directives, and pipes that belong to this module
    AppComponent,   // The root component of the application
    ChatComponent   // The chat component that handles WebSocket-based chat functionality
  ],
  imports: [
    // Import other Angular modules that are required for this module to function
    BrowserModule,  // Required for any web-based Angular application
    FormsModule     // Provides template-driven forms and two-way data binding
  ],
  providers: [],
  bootstrap: [AppComponent]  // Bootstraps the root component of the application
})
export class AppModule { }
