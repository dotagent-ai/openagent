##  Reference for nextpy/frontend/components/core/layout/center.pyi

# Nextpy Documentation: Center Component

## Overview

The `Center` component in Nextpy is designed to center its child elements. It is typically used to align content within a container and can be useful for creating layouts with a balanced visual weight.

### Purpose

The `Center` component serves the purpose of simplifying the alignment of elements by providing a straightforward way to center content horizontally and vertically within its parent.

### Use Cases

- Centering text or images on a page.
- Aligning a group of buttons or controls within a modal or form.
- Creating a splash screen with centered branding elements.

### Structure

`Center` inherits from the `Div` component, meaning it behaves like a standard HTML `<div>` element with additional properties that allow for easy centering.

## Anatomy

### Basic Implementation

```python
from nextpy.frontend.components.core.layout.center import Center

centered_content = Center.create(
    "This is a centered text block."
)
```

### Advanced Implementation

```python
from nextpy.frontend.components.core.layout.center import Center
from nextpy.frontend.style import Style

centered_content_with_style = Center.create(
    "This is a centered text block with custom styling.",
    style=Style(
        color="white",
        background_color="blue",
        padding="20px"
    )
)
```

## Components

`Center` has no additional sub-components but allows for child components to be passed to it.

### Properties Table

| Prop Name        | Type                                                 | Description                                   |
| ---------------- | ---------------------------------------------------- | --------------------------------------------- |
| `access_key`     | `Optional[Union[Var, str, int, bool]]`               | Keyboard shortcut hint for the element.       |
| `auto_capitalize`| `Optional[Union[Var, str, int, bool]]`               | Controls text capitalization as it's entered. |
| `content_editable`| `Optional[Union[Var, str, int, bool]]`              | Indicates if the element's content is editable.|
| ...              |                                                      | ...                                           |
| `style`          | `Optional[Style]`                                    | The style properties for the component.       |
| `key`            | `Optional[Any]`                                      | A unique key for the component.               |
| `id`             | `Optional[Any]`                                      | The id for the component.                     |
| `class_name`     | `Optional[Any]`                                      | The class name for the component.             |
| `autofocus`      | `Optional[bool]`                                     | Autofocuses the component when loaded.        |
| `custom_attrs`   | `Optional[Dict[str, Union[Var, str]]]`               | Custom attributes for the component.          |

### Event Triggers

| Event Name        | Type                                                 | Description                                   |
| ----------------- | ---------------------------------------------------- | --------------------------------------------- |
| `on_blur`         | `Optional[Union[EventHandler, EventSpec, list]]`     | Event fired when the component loses focus.   |
| `on_click`        | `Optional[Union[EventHandler, EventSpec, list]]`     | Event fired when the component is clicked.    |
| ...               |                                                      | ...                                           |

## Notes

- The `Center` component should not be overused as it can lead to excessive white space and unbalanced layouts if not used thoughtfully.
- When using the `Center` component, it's important to consider the dimensions of both the centered element and its parent container to achieve the desired alignment.

## Best Practices

- Use the `Center` component in moderation and where it's functionally appropriate to align content.
- Combine the `Center` component with appropriate padding and margin to maintain good spacing in your layout.
- Consider using the `style` property for customizing the appearance of the centered content to match your application's theme.

By adhering to this structure and content format, you will ensure that the documentation for the Nextpy library's `Center` component is clear, concise, complete, and developer-friendly, aligning with the standards of well-documented projects.