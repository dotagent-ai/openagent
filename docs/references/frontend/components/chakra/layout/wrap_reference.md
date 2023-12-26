##  Reference for nextpy/frontend/components/chakra/layout/wrap.pyi

# Wrap Component Documentation

## Wrap

### Overview

The `Wrap` component in Nextpy's Chakra UI library is designed to manage the layout of its child components in a responsive and flexible manner. It's similar to the flex container in CSS and automatically wraps child components based on the available space.

### Use Cases

- Arranging a list of tags or chips that need to wrap onto the next line when space is limited.
- Creating a responsive gallery of cards or images.
- Displaying a list of form inputs or buttons in a flexible layout.

### Anatomy

#### Basic Implementation

```python
from nextpy.components.chakra.layout.wrap import Wrap, WrapItem

wrap = Wrap.create(
    WrapItem.create("Item 1"),
    WrapItem.create("Item 2"),
    WrapItem.create("Item 3"),
    spacing="30px"  # defines space between items
)
```

#### Advanced Implementation

```python
wrap = Wrap.create(
    WrapItem.create("Item A"),
    WrapItem.create("Item B"),
    WrapItem.create("Item C"),
    align="center",  # aligns items vertically
    justify="space-between",  # distributes space between items horizontally
    direction="row",  # sets the direction of items
    spacing_x="20px",  # horizontal spacing
    spacing_y="10px",  # vertical spacing
    should_wrap_children=True  # wraps children in `WrapItem`
)
```

### Components

#### Properties Table

| Prop Name             | Type                    | Description                                         |
|-----------------------|-------------------------|-----------------------------------------------------|
| `children`            | `Component`             | Child components to be included within the `Wrap`.  |
| `align`               | `Var[str]`, `str`       | Vertical alignment of the child components.         |
| `direction`           | `Var[str]`, `str`       | Flex direction of the child components.             |
| `justify`             | `Var[str]`, `str`       | Horizontal justification of the child components.   |
| `should_wrap_children`| `Var[bool]`, `bool`     | If `True`, wraps children in `WrapItem`.            |
| `spacing`             | `Var[str]`, `str`       | Spacing between child components.                   |
| `spacing_x`           | `Var[str]`, `str`       | Horizontal spacing between child components.        |
| `spacing_y`           | `Var[str]`, `str`       | Vertical spacing between child components.          |
| `style`               | `Style`                 | CSS styles for the wrap component.                  |
| `key`                 | `Any`                   | A unique key for the component.                     |
| `id`                  | `Any`                   | The id for the component.                           |
| `class_name`          | `Any`                   | The class name for the component.                   |
| `custom_attrs`        | `Dict[str, Union[Var, str]]` | Custom attributes for the component.          |

#### Event Triggers

- `on_blur`: Triggered when the component loses focus.
- `on_click`: Triggered when the component is clicked.
- `on_double_click`: Triggered on a double-click on the component.
- `on_focus`: Triggered when the component gains focus.
- `on_mount`: Triggered when the component is mounted to the DOM.
- `on_mouse_down`: Triggered when a mouse button is pressed on the component.
- `on_mouse_enter`: Triggered when the mouse enters the component.
- `on_mouse_leave`: Triggered when the mouse leaves the component.
- `on_mouse_move`: Triggered when the mouse moves over the component.
- `on_mouse_up`: Triggered when a mouse button is released over the component.
- `on_scroll`: Triggered when the component is scrolled.
- `on_unmount`: Triggered when the component is unmounted from the DOM.

### Notes

When using `Wrap`, it's important to be aware that its behavior is influenced by the screen size. Therefore, you should test your layout on various screen sizes to ensure it looks and functions as expected.

### Best Practices

- Use `Wrap` for small to medium-sized sets of homogenous elements that benefit from a flexible layout.
- Always specify `spacing` for consistent visual appearance.
- Consider using `WrapItem` to control the layout of individual children when needed.
- Avoid using `Wrap` for very complex or large-scale layouts where a grid might be more appropriate.