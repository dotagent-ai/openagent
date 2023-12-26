##  Reference for nextpy/frontend/components/el/elements/base.pyi

The provided stub file seems to be a part of the generated documentation for a component named `BaseHTML` in the Nextpy library. Here's an example of how you might document this component following the documentation structure guidelines you provided:

---

# BaseHTML

## Overview

The `BaseHTML` component is the fundamental building block for creating HTML elements in Nextpy applications. It serves as the base class from which specific HTML elements are derived, providing a common interface for essential HTML attributes and events.

## Purpose

`BaseHTML` provides an abstraction over raw HTML elements, allowing developers to interact with and create elements in a type-safe and Pythonic way. It includes standard HTML attributes such as `id`, `class_name`, and `style`, as well as event handling properties such as `on_click` and `on_mouse_enter`.

## Use Cases

- Creating custom HTML elements that are not explicitly provided by Nextpy.
- Extending existing HTML elements with additional functionality.
- Abstracting complex HTML structure and behavior into reusable components.

## Structure and Usage

The `BaseHTML` component can be used to create any standard HTML element by passing appropriate children and properties.

### Anatomy

#### Basic Implementation

```python
from nextpy.components.el.elements.base import BaseHTML

# Creating a simple div element with text content
my_div = BaseHTML.create('This is a div', id='my-div')
```

#### Advanced Implementation

```python
from nextpy.components.el.elements.base import BaseHTML

# Creating a div element with nested children and event handling
my_div = BaseHTML.create(
    BaseHTML.create('Click me!', on_click=my_click_handler),
    BaseHTML.create('Child 2'),
    id='parent-div',
    class_name='my-custom-class',
    on_mouse_enter=my_mouse_enter_handler
)
```

## Components

### Properties

| Prop Name          | Type                                                   | Description                                                  |
|--------------------|--------------------------------------------------------|--------------------------------------------------------------|
| access_key         | `Optional[Union[Var[str, int, bool], str, int, bool]]` | Provides a hint for generating a keyboard shortcut.          |
| auto_capitalize    | `Optional[Union[Var[str, int, bool], str, int, bool]]` | Controls automatic capitalization of text input.             |
| content_editable   | `Optional[Union[Var[str, int, bool], str, int, bool]]` | Indicates whether the element's content is editable.         |
| ...                | ...                                                    | ...                                                          |

### Event Triggers

| Event Name      | Handler Type                                     | Description                        |
|-----------------|--------------------------------------------------|------------------------------------|
| on_blur         | `Optional[Union[EventHandler, EventSpec, ...]]`  | Triggered when the element loses focus. |
| on_click        | `Optional[Union[EventHandler, EventSpec, ...]]`  | Triggered when the element is clicked.  |
| ...             | ...                                              | ...                                |

## Notes

- Ensure that event handlers are provided as callable functions or `BaseVar` instances.
- Custom attributes can be provided through the `custom_attrs` property.

## Best Practices

- Use meaningful `id` and `class_name` to facilitate CSS styling and JavaScript interactions.
- Only set `autofocus` on elements that should immediately engage the user.
- Utilize `on_mount` and `on_unmount` for initialization and cleanup tasks in the component lifecycle.

--- 

This documentation provides a clear and concise overview of the `BaseHTML` component, its purpose, how to use it, detailed property and event descriptions, important notes, and best practices for utilizing the component effectively.