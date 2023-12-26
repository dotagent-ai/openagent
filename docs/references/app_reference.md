##  Reference for nextpy/app.pyi

# Nextpy Documentation

Welcome to the Nextpy documentation. This guide provides an overview of the Nextpy library, a Python framework for building full-stack applications. Inspired by Streamlit, Nextpy aims to provide a fast and efficient way to create interactive and modern web applications using Python.

## Table of Contents

- **Introduction**
  - What is Nextpy?
  - Key Features
- **Getting Started**
  - Installation
  - Quick Start Guide
- **Components**
  - App
  - Component
  - State
  - Event
  - Middleware
  - AdminDash
- **Advanced Topics**
  - Event Handling
  - State Management
  - Custom Middleware
  - Asynchronous Operations
- **Best Practices**
- **API Reference**
  - Public API Overview
- **Contributing**
  - How to Contribute
  - Code of Conduct
- **Changelog**

---

## Introduction

### What is Nextpy?

Nextpy is a powerful Python library for building full-stack web applications. It leverages modern web technologies, enabling developers to craft interactive user interfaces, manage application state, and handle events seamlessly with Python code.

### Key Features

- **Full-Stack Capabilities**: Create the front-end and back-end of your application in Python.
- **Component-Based**: Build reusable UI components that can be combined to create complex interfaces.
- **Event-Driven Architecture**: Respond to user actions and other events in real-time.
- **State Management**: Maintain the state of your application with a clear and concise API.
- **Admin Dashboard**: Monitor and manage your application with an integrated admin dashboard.

## Getting Started

### Installation

To install Nextpy, run the following command in your terminal:

```bash
pip install nextpy
```

### Quick Start Guide

Create your first Nextpy application by following these simple steps:

1. Import the necessary modules from Nextpy.
2. Create an instance of the `App` class.
3. Define components and add them to your app.
4. Start your application.

Here's a basic example:

```python
from nextpy import App, Component

class MyComponent(Component):
    def render(self):
        return "<div>Hello, Nextpy!</div>"

app = App()
app.add_page(MyComponent(), route='/')

if __name__ == '__main__':
    app.compile()
```

## Components

### App

The `App` class is the central part of a Nextpy application. It manages pages, stylesheets, the API server, and more.

#### Anatomy

- **Initialization**:
  - Create an App instance with optional style and admin dashboard parameters.
- **Methods**:
  - `add_page()`: Add a new page to the application.
  - `add_middleware()`: Include custom middleware.
  - `compile()`: Compile the application frontend and backend.

```python
app = App(stylesheets=['style.css'])
```

### Component

Components are the building blocks of Nextpy applications. They define the UI elements and their behavior.

#### Anatomy

- **Component Structure**:
  - Every component must inherit from the `Component` class and implement the `render()` method.

```python
class MyComponent(Component):
    def render(self):
        return "<button>Click Me</button>"
```

### State

State objects hold the application's state and provide methods to update it safely.

#### Anatomy

- **State Management**:
  - Access and manipulate the application's state using the `State` class.

```python
from nextpy import State

state = State({'counter': 0})
state.update({'counter': state['counter'] + 1})
```

### Event

Events in Nextpy are actions triggered by user interactions or other sources, used to update the application state.

#### Anatomy

- **Event Handling**:
  - Define custom events and handle them to perform state updates.

```python
from nextpy import Event

def handle_click(event: Event):
    # Update state in response to the event
    pass
```

### Middleware

Middleware in Nextpy allows developers to modify the request or response of an application.

#### Anatomy

- **Custom Middleware**:
  - Create middleware by inheriting from the `Middleware` class.

```python
from nextpy import Middleware

class CustomMiddleware(Middleware):
    async def process_request(self, request):
        # Process the request
        pass
```

### AdminDash

AdminDash provides an administrative dashboard for monitoring and managing the application.

#### Anatomy

- **Admin Dashboard**:
  - Enable and configure the admin dashboard within the `App` instance.

```python
app = App(admin_dash=AdminDash())
```

## Advanced Topics

These sections cover in-depth features such as event handling, state management, custom middleware, and handling asynchronous operations.

## Best Practices

Guidelines for writing efficient and maintainable Nextpy applications, including tips on component design, state management, and performance optimization.

## API Reference

A comprehensive guide to the Nextpy public API, detailing classes, methods, properties, and events.

## Contributing

Information on how to contribute to the Nextpy project, including submitting pull requests, reporting issues, and participating in the community.

## Changelog

A record of all the changes made to Nextpy, including new features, bug fixes, and improvements.

---

This overview provides a foundational understanding of Nextpy. For detailed information on each component and feature, refer to the corresponding section in the documentation. Happy coding!