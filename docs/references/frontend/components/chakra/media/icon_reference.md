##  Reference for nextpy/frontend/components/chakra/media/icon.pyi

# Nextpy Library Documentation

## Icon

### Overview

The `Icon` component in the Nextpy library is used to include icons from a set of predefined iconography within a Nextpy application. Icons are visual symbols that can represent actions, items, or concepts and are commonly used in user interfaces to enhance the user experience.

### Purpose and Use Cases

Icons are typically used to:

- Provide visual cues that support text labels, making it easier for users to recognize functions or options.
- Save space on the user interface by substituting lengthy text descriptions.
- Enhance the aesthetic appeal of the application.
- Create a more intuitive user interface.

### Structure and Usage

The `Icon` component is created using the `create` method. It can accept various arguments such as style, key, id, class name, autofocus, custom attributes, event handlers, and additional props.

### Anatomy

#### Basic Implementation

```python
from nextpy.components.chakra.media import Icon

# Create an icon with default style
my_icon = Icon.create(name="check-circle")
```

#### Advanced Implementation

```python
from nextpy.components.chakra.media import Icon
from nextpy.frontend.style import Style

# Create an icon with custom style and event handlers
custom_style = Style(color="green", width="24px", height="24px")
my_icon = Icon.create(
    name="check-circle",
    style=custom_style,
    on_click=lambda event: print("Icon clicked")
)
```

### Components

The `Icon` component can be customized with the following properties and event triggers.

#### Properties Table

| Prop Name      | Type         | Description                               |
| -------------- | ------------ | ----------------------------------------- |
| `name`         | `str`        | The name of the icon to be displayed.     |
| `style`        | `Style`      | The styling of the icon component.        |
| `key`          | `Any`        | A unique key for the component.           |
| `id`           | `Any`        | The id for the component.                 |
| `class_name`   | `Any`        | The class name for the component.         |
| `autofocus`    | `bool`       | Autofocus on component when page loads.   |
| `custom_attrs` | `Dict`       | Custom attributes for the component.      |

#### Event Triggers

| Event Name         | Description                                  |
| ------------------ | -------------------------------------------- |
| `on_blur`          | Event when the component loses focus.        |
| `on_click`         | Event when the component is clicked.         |
| `on_context_menu`  | Event when the context menu is accessed.     |
| `on_double_click`  | Event when the component is double-clicked.  |
| `on_focus`         | Event when the component gains focus.        |
| `on_mount`         | Event when the component is mounted.         |
| `on_mouse_down`    | Event when mouse button is pressed.          |
| `on_mouse_enter`   | Event when mouse enters the component area.  |
| `on_mouse_leave`   | Event when mouse leaves the component area.  |
| `on_mouse_move`    | Event when mouse moves over the component.   |
| `on_mouse_out`     | Event when mouse moves out of the component. |
| `on_mouse_over`    | Event when mouse is over the component.      |
| `on_mouse_up`      | Event when mouse button is released.         |
| `on_scroll`        | Event when the component is scrolled.        |
| `on_unmount`       | Event when the component is unmounted.       |

### Notes

- Always provide an accessible name for icons when they represent interactive elements.
- When using icons for decoration, ensure they are hidden from assistive technologies to avoid redundancy.

### Best Practices

- Use icons consistently within your application to maintain a cohesive design language.
- Ensure that the icon's purpose is clear and does not rely solely on color to convey information.
- Provide alternative text for icons used as buttons or links to ensure accessibility.
- Keep icons simple and easy to understand.
- Use an appropriate size for icons to ensure they are easily clickable on touch devices.

The `ICON_LIST` constant contains the names of all available icons. When specifying the `name` property, ensure that it matches one of the names listed in `ICON_LIST`.