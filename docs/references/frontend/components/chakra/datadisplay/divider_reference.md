##  Reference for nextpy/frontend/components/chakra/datadisplay/divider.pyi

# Nextpy Documentation: Divider Component

## Divider

The `Divider` component is a visual element that can be used to separate content within a layout. It can be oriented horizontally or vertically and supports different variants such as solid or dashed lines. This component is useful in organizing the content of a web application, enhancing its readability and structure.

### Anatomy

The `Divider` component is simple to implement. Here are some code snippets showing both basic and advanced usage.

#### Basic Usage:

```python
from nextpy.components.chakra.datadisplay import Divider

# Horizontal Divider
divider_horizontal = Divider.create(orientation="horizontal")

# Vertical Divider (Ensure the parent element has a specified height)
divider_vertical = Divider.create(orientation="vertical")
```

#### Advanced Usage:

Custom styling and variants can be added to make the `Divider` fit better within the design of the application.

```python
from nextpy.components.chakra.datadisplay import Divider
from nextpy.frontend.style import Style

# Custom Styled Horizontal Solid Divider
custom_style = Style(border_color="gray.200", border_width=2)
divider_horizontal_custom = Divider.create(
    orientation="horizontal", 
    variant="solid", 
    style=custom_style
)

# Vertical Dashed Divider with an ID and class
divider_vertical_dashed = Divider.create(
    orientation="vertical", 
    variant="dashed",
    id="my-divider",
    class_name="custom-divider-class"
)
```

### Components

#### Properties

| Prop Name      | Type                                                   | Description                                                                              |
| -------------- | ------------------------------------------------------ | ---------------------------------------------------------------------------------------- |
| `orientation`  | `Var[Literal["horizontal", "vertical"]]` or literals  | Sets the orientation of the divider to either horizontal or vertical.                    |
| `variant`      | `Var[Literal["solid", "dashed"]]` or literals         | The visual style of the divider (solid or dashed).                                       |
| `style`        | `Style`                                                | Allows custom styling to be applied to the component.                                    |
| `key`          | Any                                                    | A unique key that identifies the component.                                              |
| `id`           | Any                                                    | The HTML id attribute of the component.                                                  |
| `class_name`   | Any                                                    | The HTML class attribute for the component.                                              |
| `autofocus`    | `bool`                                                 | If set to `True`, the component will automatically focus when the page loads.            |
| `custom_attrs` | `Dict[str, Union[Var, str]]`                           | Allows custom attributes to be added to the component.                                   |

#### Event Triggers

| Event Name         | Description                                                        |
| ------------------ | ------------------------------------------------------------------ |
| `on_blur`          | Event triggered when the component loses focus.                    |
| `on_click`         | Event triggered when the component is clicked.                     |
| `on_context_menu`  | Event triggered when the context menu is requested on the element. |
| `on_double_click`  | Event triggered on a double-click on the component.                |
| `on_focus`         | Event triggered when the component gains focus.                    |
| `on_mount`         | Event triggered when the component is mounted.                     |
| `on_mouse_down`    | Event triggered when a mouse button is pressed on the component.   |
| `on_mouse_enter`   | Event triggered when the mouse enters the component area.          |
| `on_mouse_leave`   | Event triggered when the mouse leaves the component area.          |
| `on_mouse_move`    | Event triggered when the mouse moves over the component.           |
| `on_mouse_out`     | Event triggered when the mouse is moved out of the component.      |
| `on_mouse_over`    | Event triggered when the mouse is moved over the component.        |
| `on_mouse_up`      | Event triggered when a mouse button is released over the component.|
| `on_scroll`        | Event triggered when the component is scrolled.                     |
| `on_unmount`       | Event triggered when the component is unmounted.                   |

### Notes

- When using the `vertical` orientation for the `Divider`, ensure that the parent container has a specified height, otherwise, the divider may not be visible.
- Custom styling can be achieved using the `Style` class. Be mindful of the existing styling provided by Chakra to prevent conflicts.

### Best Practices

- Use the `Divider` component to create clear visual separations between different sections or elements of your application.
- Choose an appropriate variant (`solid` or `dashed`) that complements the design language of your application.
- When applying custom styles, consider the overall design consistency and ensure accessibility standards are maintained, such as sufficient contrast for visibility.
- Ensure that interactive elements around the divider remain accessible and that the divider itself does not cause confusion by appearing clickable when it is not intended to be an interactive element.