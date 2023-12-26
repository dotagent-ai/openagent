##  Reference for nextpy/frontend/components/radix/themes/layout/container.pyi

# Container Component

## Overview

The `Container` component in the Nextpy library is a layout utility that encapsulates its children, providing a way to control the width and padding of the content within it. It serves as a fundamental building block for creating structured and responsive layouts in full-stack Python applications.

## Anatomy

### Basic Usage

To create a basic `Container`, you simply need to call its `create` method and pass any child components as arguments:

```python
from nextpy.components.radix.themes.layout.container import Container

content_container = Container.create(
    # child components here
)
```

### Advanced Usage

The `Container` component provides several optional parameters to control its appearance and behavior. For instance, to set padding and color scheme, you can do the following:

```python
from nextpy.components.radix.themes.layout.container import Container

advanced_container = Container.create(
    # child components here
    p="3",  # padding
    color_scheme="blue",  # color scheme
)
```

## Components

### Properties Table

| Prop Name       | Type                         | Description                                                 |
|-----------------|------------------------------|-------------------------------------------------------------|
| `color`         | `Var[str]`, `str`            | Maps to CSS color property.                                 |
| `color_scheme`  | `Var[Literal[...]]`, `str`   | Maps to radix color property, defined by a set of literals. |
| `size`          | `Var[LiteralContainerSize]`, `str` | The size of the container: "1" - "4" (default "4").   |
| `p`, `px`, `py` | `Var[Literal[...]]`, `str`   | Padding properties with predefined scale values.            |
| `m`, `mx`, `my` | `Var[Literal[...]]`, `str`   | Margin properties with predefined scale values.             |
| `style`         | `Style`                      | The CSS style of the component.                             |
| `key`           | `Any`                        | A unique key for the component.                             |
| `id`            | `Any`                        | The ID for the component.                                   |
| `class_name`    | `Any`                        | The class name for the component.                           |
| `...`           | `...`                        | Other HTML attributes and event handlers.                   |

### Event Triggers

- `on_blur`
- `on_click`
- `on_context_menu`
- `on_double_click`
- `on_focus`
- `on_mouse_down`
- `on_mouse_enter`
- `on_mouse_leave`
- `on_mouse_move`
- `on_mouse_out`
- `on_mouse_over`
- `on_mouse_up`
- `on_scroll`

## Notes

- When using `Container`, ensure that it is compatible with the layout structure of your application. Nesting containers can affect the responsiveness of the layout.
- If using a predefined color scheme, make sure it aligns with the application's design system.

## Best Practices

- Use `Container` to control the width of sections of your application for a consistent layout across different screen sizes.
- Combine padding and margin props (`p`, `px`, `py`, `m`, `mx`, `my`) thoughtfully to achieve the desired spacing without over-complicating the layout.
- Use `size` to standardize the maximum width of containers throughout your app, providing a harmonious visual experience.
- Remember that `Container` is a div element at its core; use semantic HTML where appropriate for better accessibility and SEO.

By adhering to these guidelines and understanding the structure of `Container`, developers can effectively use this component to build clean and responsive interfaces.