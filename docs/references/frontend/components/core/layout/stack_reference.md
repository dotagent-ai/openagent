##  Reference for nextpy/frontend/components/core/layout/stack.pyi

# Stack Component

## Overview

The `Stack` component in Nextpy is a layout utility designed to stack its child components either vertically or horizontally, with customizable alignment and spacing. It is built on top of the `Div` element, providing an easy way to organize UI elements in a structured and consistent manner.

## Use Cases

- Stacking form inputs with labels for a clean look.
- Arranging buttons or icons in a toolbar.
- Displaying a list of items such as messages or notifications.
- Creating a layout for cards or tiles in a grid-like fashion.

## Anatomy

### Basic Usage

```python
from nextpy.frontend.components.core.layout.stack import HStack, VStack

# Horizontal Stack
horizontal_stack = HStack.create(
    Div(text="Item 1"),
    Div(text="Item 2"),
    justify="start",
    align="center",
    spacing="1rem"
)

# Vertical Stack
vertical_stack = VStack.create(
    Div(text="Item A"),
    Div(text="Item B"),
    justify="center",
    align="stretch",
    spacing="2rem"
)
```

### Advanced Usage

```python
# Advanced HStack with custom attributes and event handling
advanced_hstack = HStack.create(
    Div(text="Clickable Item", on_click=lambda event: print("Item clicked")),
    Div(text="Hidden Item", hidden=True),
    justify="space-between",
    align="center",
    spacing="1rem",
    style=Style(margin="10px"),
    custom_attrs={"data-type": "advanced-stack"}
)
```

## Components

### `Stack`

- **Overview**: Acts as a base component for `HStack` and `VStack`.
- **Properties**:
  
  | Prop Name           | Type                                              | Description                                             |
  |---------------------|---------------------------------------------------|---------------------------------------------------------|
  | `justify`           | `Optional[LiteralJustify]`                        | Justifies child elements horizontally within the stack. |
  | `align`             | `Optional[LiteralAlign]`                          | Aligns child elements vertically within the stack.       |
  | `spacing`           | `Optional[str]`                                   | Defines the space between child elements.               |
  | *Inherited Props*   | *from `Div`*                                      | *See `Div` documentation for additional props.*         |

- **Event Triggers**: Inherits event triggers from `Div`.

### `HStack`

- **Overview**: A specialized stack that aligns items horizontally.
- **Usage**: Similar to `Stack`, with default `justify` and `align` suited for horizontal layouts.

### `VStack`

- **Overview**: A specialized stack that aligns items vertically.
- **Usage**: Similar to `Stack`, with default `justify` and `align` suited for vertical layouts.

## Notes

- The `spacing` attribute should be a valid CSS unit (e.g., `rem`, `em`, `px`).
- Attributes such as `hidden` or `custom_attrs` allow for further customization and conditional rendering.

## Best Practices

- Use `HStack` for horizontal arrangements and `VStack` for vertical arrangements to leverage default styling suited for each orientation.
- Use `spacing` to maintain consistent gaps between elements, which helps with the overall visual rhythm of the layout.
- When using event triggers like `on_click`, ensure that callback functions are defined in a way that does not cause unnecessary re-renders.
- Utilize `style` prop to add custom styles but avoid inline styles for complex CSS, which can be moved to a separate stylesheet for better maintainability.

## Helper Functions

- `hstack`: A convenience function to create an `HStack`.
- `vstack`: A convenience function to create a `VStack`.

```python
# Using helper functions
horizontal_stack = hstack(
    Div(text="Item 1"),
    Div(text="Item 2"),
    spacing="1rem"
)

vertical_stack = vstack(
    Div(text="Item A"),
    Div(text="Item B"),
    spacing="2rem"
)
```

By adhering to this structure, developers can utilize the `Stack` component to create organized and responsive layouts with ease.