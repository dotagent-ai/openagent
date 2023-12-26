##  Reference for nextpy/frontend/components/core/layout/spacer.pyi

# Nextpy Documentation: Spacer Component

## Overview

The Spacer component is designed to create empty spaces in your layouts, allowing you to control the padding and margins between other components without having to directly manipulate their styling. It is particularly useful in situations where you want to maintain a clean separation of concerns by not embedding spacing directly into components that have other primary functionalities.

## Use Cases

- Separating elements horizontally or vertically without altering their properties.
- Creating consistent spacing in a grid or flex layout.
- Filling empty areas to push content towards a preferred direction on the screen.

## Anatomy

The `Spacer` component is essentially a `Div` element with the capability to provide space within your user interface. Here are some basic and advanced examples:

### Basic Usage

```python
from nextpy.frontend.components.core.layout import spacer

# Creating a simple spacer with default properties
simple_spacer = spacer.create()
```

### Advanced Usage

```python
from nextpy.frontend.components.core.layout import spacer
from nextpy.frontend.style import Style

# Creating a spacer with a specific height and width
custom_spacer = spacer.create(style=Style(height='50px', width='100%'))
```

## Components

The `Spacer` component is a single entity without any sub-components. However, it can be styled and customized using the following properties:

| Prop Name         | Type                             | Description                                                   |
|-------------------|----------------------------------|---------------------------------------------------------------|
| `access_key`      | `str \| int \| bool \| Var`      | Provides a keyboard shortcut for the element.                 |
| `auto_capitalize` | `str \| int \| bool \| Var`      | Controls text input capitalization.                           |
| ...               | ...                              | ...                                                           |
| `style`           | `Style`                          | The style of the component, such as height, width, etc.       |
| `key`             | `Any`                            | A unique key for the component.                               |
| `id`              | `Any`                            | The ID for the component.                                     |
| `class_name`      | `Any`                            | The class name for the component.                             |
| `autofocus`       | `bool`                           | Whether the component should autofocus.                       |
| `custom_attrs`    | `Dict[str, Union[Var, str]]`     | Additional custom attributes for the component.               |
| ...               | ...                              | ...                                                           |

## Notes

- The `Spacer` component doesn't render any visible content on its own and is purely used for spacing purposes.
- It's important to use spacers judiciously to prevent excessive white space or unbalanced layouts.

## Best Practices

- Use the `Spacer` component instead of applying margins and paddings directly to elements when you need to adjust the layout.
- Combine the `Spacer` with responsive design techniques to ensure that spacing adjusts appropriately across different screen sizes.
- Utilize the styling options to set the size of the `Spacer` based on the design requirements without resorting to extra containers or wrappers.

Remember, the goal of the `Spacer` component is to simplify the layout process and maintain the visual structure of your application without introducing unnecessary complexity.