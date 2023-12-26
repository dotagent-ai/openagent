##  Reference for nextpy/frontend/components/radix/themes/layout/base.pyi

# Layout Component

## Overview

The `LayoutComponent` is a foundational element within the Nextpy library that's designed to provide developers with a flexible container for arranging and styling child components in a full-stack Python application. It's part of the Radix Themes collection and inherits common margin properties to aid in consistent and responsive spacing throughout the UI design.

## Purpose

The purpose of the `LayoutComponent` is to offer a versatile and easy-to-use way to manage layout and spacing in web applications. It encapsulates common layout patterns such as padding, margin, color schemes, and the ability to grow or shrink elements within the available space, providing a coherent visual structure.

## Use Cases

- **Responsive Design**: Easily adjust spacing and layout for different screen sizes using the provided props.
- **Consistent Spacing**: Maintain a uniform look and feel throughout the application with predefined spacing scales.
- **Visual Grouping**: Organize related UI elements together to improve user experience.
- **Flexible Layouts**: Combine with other components to create complex UI structures.

## Structure and Usage

A `LayoutComponent` is a container that can hold other elements or components. It controls how its children are displayed and spaced using a variety of props that map to CSS properties. Below are some of the key properties and their intended use.

### Props

- `color`: Maps to the CSS default color property.
- `color_scheme`: Applies pre-defined color themes from Radix.
- `p`, `px`, `py`, `pt`, `pr`, `pb`, `pl`: Control padding on all sides, horizontal, vertical, top, right, bottom, and left respectively.
- `shrink`, `grow`: Determine how the component should fit within its container.
- `m`, `mx`, `my`, `mt`, `mr`, `mb`, `ml`: Control margin similarly to padding.
- `style`: Apply additional CSS styles.
- `key`: Assign a unique key for React's rendering system.
- `id`: Set the HTML id attribute.
- `class_name`: Apply custom CSS classes.

### Anatomy

#### Basic Implementation

```python
from nextpy.components.radix.themes.layout.base import LayoutComponent

# Create a layout component with default properties
layout = LayoutComponent.create(
    # children components go here
)

# Create a layout with custom padding and color scheme
custom_layout = LayoutComponent.create(
    # children components go here
    p="4",
    color_scheme="blue"
)
```

#### Advanced Implementation

```python
from nextpy.components.radix.themes.layout.base import LayoutComponent

# Advanced layout with multiple custom properties
advanced_layout = LayoutComponent.create(
    # children components go here
    px="3",
    py="2",
    mt="5",
    mb="2",
    color="white",
    color_scheme="indigo",
    grow="1",
    style=Style(border="1px solid #ddd")
)
```

## Components

The `LayoutComponent` does not have sub-components, as it serves as a container for other components.

## Notes

- The `LayoutComponent` should not be overly nested as it may affect performance and readability.
- Padding and margin props follow a scale from "1" to "9"; it is advisable to stick to this scale for consistency across the UI.

## Best Practices

- Use the `LayoutComponent` to group related elements for better semantic structure.
- Avoid mixing too many layout props on a single component; try to keep styling focused and intentional.
- Utilize the `color_scheme` prop to leverage the built-in color palettes for a professional look.
- Remember that `grow` and `shrink` can affect the layout significantly, especially in flexbox layouts, so use them judiciously.
- When applying custom styles, consider extending the `Style` object to maintain clean code and reusability.

By following these guidelines and utilizing the `LayoutComponent` effectively, developers can create well-structured and visually appealing web applications using the Nextpy library.