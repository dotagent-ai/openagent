##  Reference for nextpy/frontend/components/base/body.pyi

# Body Component Documentation

## Overview

The `Body` component is a fundamental building block in the Nextpy library, used to define the main content area of a web application or web page. It is analogous to the HTML `<body>` element and serves as a container for other components that together make up the user interface.

### Purpose

The purpose of the `Body` component is to provide a structured area where other UI components can be placed and styled. It is typically used as the root component that holds the layout of the entire application.

### Use Cases

The `Body` component is used in scenarios such as:

- Creating the main layout for a web application.
- Structuring the content area for sections, navigation, and other UI elements.
- Implementing page-specific layouts with custom styling and behavior.

## Anatomy

### Basic Implementation

Here is a simple example of how to use the `Body` component:

```python
from nextpy.frontend.components.base.body import Body

# Create a Body component with a child component
body = Body.create(
    "Hello, Nextpy!",
    style=Style(background_color="#f0f0f0")
)
```

### Advanced Implementation

For a more advanced usage that involves event handling and custom attributes:

```python
from nextpy.frontend.components.base.body import Body
from nextpy.backend.event import EventHandler

def on_click_handler(event):
    print("Body clicked!")

body = Body.create(
    "Click me!",
    on_click=EventHandler(on_click_handler),
    custom_attrs={"data-custom": "value"}
)
```

## Components

The `Body` component accepts the following sub-components as children:

- Any valid Nextpy component that can be nested within the body of the application.

### Properties

| Prop Name       | Type                                                       | Description                                                   |
|-----------------|------------------------------------------------------------|---------------------------------------------------------------|
| `style`         | `Optional[Style]`                                          | The style to apply to the component.                          |
| `key`           | `Optional[Any]`                                            | A unique key for the component.                               |
| `id`            | `Optional[Any]`                                            | The DOM id for the component.                                 |
| `class_name`    | `Optional[Any]`                                            | The CSS class name for the component.                         |
| `autofocus`     | `Optional[bool]`                                           | Whether the component should autofocus on page load.          |
| `custom_attrs`  | `Optional[Dict[str, Union[Var, str]]]`                     | Custom attributes for the component.                          |
| `on_blur`       | `Optional[Union[EventHandler, EventSpec, list, function]]` | Event handler for the blur event.                             |
| ...             | ...                                                        | ...                                                           |
| `on_unmount`    | `Optional[Union[EventHandler, EventSpec, list, function]]` | Event handler for when the component is unmounted.            |

Note: This table doesn't list all properties. Please refer to the stub file for a complete list of event properties.

### Event Triggers

The `Body` component supports various event triggers, such as:

- `on_click`: Triggered when the component is clicked.
- `on_double_click`: Triggered on a double-click event.
- `on_mouse_enter`: Triggered when the mouse pointer enters the component.
- `on_scroll`: Triggered when scrolling within the component.

## Notes

- It is important to ensure that the `key` property is unique amongst all sibling components to maintain component state and identity across renders.
- The `style` property should be used to define CSS properties in a Pythonic way, utilizing the `Style` object from `nextpy.frontend.style`.

## Best Practices

- When using the `Body` component, ensure it encapsulates the entire UI structure required for the page or application it represents.
- Utilize event handlers to make the application interactive and responsive to user actions.
- Apply custom attributes sparingly and only when necessary to avoid unnecessary complexity in the DOM.
- Always test the accessibility of your application, ensuring that the use of `autofocus` and other attributes does not hinder the experience for users relying on assistive technologies.