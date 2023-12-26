##  Reference for nextpy/frontend/components/radix/themes/components/aspectratio.pyi

# Nextpy Documentation: AspectRatio Component

## Component Name: AspectRatio

### Overview

The `AspectRatio` component is used to embed content within a container that maintains a specified aspect ratio. This is commonly used for responsive images, videos, and embeds to ensure that the aspect ratio is preserved regardless of the container's width.

### Use Cases

- Embedding a video player that maintains a 16:9 aspect ratio.
- Displaying images within a responsive grid that requires consistent shapes.
- Creating a card component with a fixed aspect ratio preview area.

### Anatomy

#### Basic Implementation

```python
from nextpy.components.radix.themes.components.aspectratio import AspectRatio

# Create an aspect ratio component with a 16:9 ratio
aspect_ratio_component = AspectRatio.create(
    ratio=16/9,
    children="Your content here"
)
```

#### Advanced Implementation

```python
from nextpy.components.radix.themes.components.aspectratio import AspectRatio

# Advanced aspect ratio with custom color scheme, margin, and event handlers
aspect_ratio_component = AspectRatio.create(
    ratio=4/3,
    color_scheme="blue",
    m="2",
    on_click=lambda event: print("Clicked!"),
    children=[
        # Insert child components or content here
    ]
)
```

### Components

#### Properties Table

| Prop Name      | Type                                            | Description                                |
| -------------- | ----------------------------------------------- | ------------------------------------------ |
| color          | `Optional[Union[Var[str], str]]`                | Maps to CSS default color property.        |
| color_scheme   | `Optional[Union[Var[Literal[...]], Literal[...]]]` | Maps to Radix color scheme.                |
| ratio          | `Optional[Union[Var[Union[float, int]], Union[float, int]]]` | The aspect ratio of the element.           |
| m              | `Optional[Union[Var[LiteralSwitchSize], LiteralSwitchSize]]` | Margin size from "1" to "9".              |
| mx             | `...`                                           | Horizontal margin size.                    |
| my             | `...`                                           | Vertical margin size.                      |
| mt             | `...`                                           | Margin top size.                           |
| mr             | `...`                                           | Margin right size.                         |
| mb             | `...`                                           | Margin bottom size.                        |
| ml             | `...`                                           | Margin left size.                          |
| style          | `Optional[Style]`                               | The style of the component.                |
| key            | `Optional[Any]`                                 | A unique key for the component.            |
| id             | `Optional[Any]`                                 | The id for the component.                  |
| class_name     | `Optional[Any]`                                 | The class name for the component.          |
| autofocus      | `Optional[bool]`                                | Autofocus the component on page load.      |
| custom_attrs   | `Optional[Dict[str, Union[Var, str]]]`          | Custom attributes for the component.       |
| on_blur        | `Optional[Union[EventHandler, EventSpec, ...]]` | Event handler for blur event.              |
| on_click       | `...`                                           | Event handler for click event.             |
| on_context_menu| `...`                                           | Event handler for context menu event.      |
| on_double_click| `...`                                           | Event handler for double click event.      |
| on_focus       | `...`                                           | Event handler for focus event.             |
| on_mount       | `...`                                           | Event handler for mount event.             |
| on_mouse_down  | `...`                                           | Event handler for mouse down event.        |
| on_mouse_enter | `...`                                           | Event handler for mouse enter event.       |
| on_mouse_leave | `...`                                           | Event handler for mouse leave event.       |
| on_mouse_move  | `...`                                           | Event handler for mouse move event.        |
| on_mouse_out   | `...`                                           | Event handler for mouse out event.         |
| on_mouse_over  | `...`                                           | Event handler for mouse over event.        |
| on_mouse_up    | `...`                                           | Event handler for mouse up event.          |
| on_scroll      | `...`                                           | Event handler for scroll event.            |
| on_unmount     | `...`                                           | Event handler for unmount event.           |

### Notes

- The `ratio` property is crucial as it determines the aspect ratio of the content.
- Event handlers such as `on_click` can be used to interact with the component.
- Custom attributes and styles can be applied for further customization.

### Best Practices

- Use meaningful ratios that represent common aspect ratios (e.g., 16:9, 4:3, etc.) for the best user experience.
- When nesting interactive components inside the `AspectRatio`, ensure that the event handlers do not conflict.
- Keep margins and padding consistent with the design system to maintain a coherent look and feel across your application.

Remember to update this documentation if the `AspectRatio` component's API changes or if new features are added to ensure that developers have the latest information for integrating this component into their projects.