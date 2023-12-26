##  Reference for nextpy/frontend/components/next/base.pyi

# NextComponent Documentation

## Overview

`NextComponent` is a foundational element in the Nextpy framework, serving as the base class for all Nextpy components. It encapsulates the common features and behaviors that are shared across various UI elements in the library, allowing for a consistent and extensible approach to component development.

## Purpose

The `NextComponent` class provides the core functionalities required for creating interactive and dynamic user interfaces in Python applications. It abstracts away the complexities of handling UI state, events, and rendering, making it easier for developers to build full-stack applications with Python.

## Use Cases

This class is used as the superclass for all Nextpy components, which means any custom component will inherit from `NextComponent`. It is the starting point for creating new UI elements, such as buttons, text inputs, lists, and other interactive components.

## Anatomy

### Basic Implementation

```python
from nextpy.components.next.base import NextComponent

class MyCustomComponent(NextComponent):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        # Custom initialization code here

    # Define custom methods and properties here
```

### Advanced Implementation

```python
from nextpy.components.next.base import NextComponent
from nextpy.frontend.style import Style

class MyAdvancedComponent(NextComponent):
    @classmethod
    def create(cls, *children, style=None, **props):
        # Define custom attributes or behaviors
        custom_style = Style({...}) if style is None else style
        return super().create(*children, style=custom_style, **props)

    # Additional advanced customization
```

## Components

### Sub-components

`NextComponent` can contain children, which can be other `NextComponent` instances or primitive data types that are renderable in the UI.

### Properties Table

| Prop Name       | Type                                                | Description                                                         |
|-----------------|-----------------------------------------------------|---------------------------------------------------------------------|
| `style`         | `Optional[Style]`                                   | The style applied to the component.                                 |
| `key`           | `Optional[Any]`                                     | A unique key to identify the component in the DOM.                  |
| `id`            | `Optional[Any]`                                     | The DOM id attribute of the component.                              |
| `class_name`    | `Optional[Any]`                                     | The CSS class name for the component.                               |
| `autofocus`     | `Optional[bool]`                                    | If set, the component will be focused automatically on page load.   |
| `custom_attrs`  | `Optional[Dict[str, Union[Var, str]]]`              | Custom HTML attributes for the component.                           |
| `on_blur`       | `Optional[Union[EventHandler, EventSpec, list, ...]` | Event handler for the blur event.                                   |
| `on_click`      | `Optional[Union[EventHandler, EventSpec, list, ...]` | Event handler for the click event.                                  |
| ...             | ...                                                 | ...                                                                 |
| `on_unmount`    | `Optional[Union[EventHandler, EventSpec, list, ...]` | Event handler that is called before the component is unmounted.     |

_Note: This table does not include all properties for brevity. Please refer to the source code for the full list._

### Event Triggers

The event properties such as `on_blur`, `on_click`, `on_focus`, etc., take a callable or an instance of `EventHandler` or `EventSpec` which will be triggered when the respective event occurs.

## Notes

- It is important to ensure that the `key` prop is unique within the same level of the component hierarchy to maintain proper state and identity across re-renders.
- Custom attributes via `custom_attrs` should be used sparingly and only when necessary, as they may affect accessibility and maintainability.

## Best Practices

- When extending `NextComponent`, always call `super().__init__(*args, **kwargs)` to ensure that all base initializations are completed.
- Use the `style` property to apply consistent styling to your components. Avoid inline styles for more complex CSS rules and use a separate stylesheet instead.
- Leverage event properties to create interactive components, ensuring that user interactions are properly handled and state is managed effectively.
- Component keys should be stable, predictable, and unique to avoid unnecessary re-renders and preserve component state.
- Document any custom properties or methods in your subclass of `NextComponent` to maintain clarity and ease of use for other developers.