##  Reference for nextpy/frontend/components/chakra/forms/iconbutton.pyi

# Nextpy Documentation: IconButton Component

## IconButton

### Overview

The `IconButton` component in the Nextpy library is designed to provide developers with a flexible and customizable button that includes an icon instead of text, enhancing the user interface with visual cues. It is commonly used in toolbars, form actions, and inline actions within content.

### Purpose

The primary purpose of the `IconButton` component is to capture user interaction in a visually appealing and intuitive manner. Icons can succinctly convey the action that will be performed, saving space and improving the overall aesthetic of the application.

### Use Cases

- Toolbars with limited space where icons are more effective than text.
- Mobile applications where screen real estate is at a premium.
- User interfaces that require a clean and modern aesthetic.
- Interactive lists or tables where actions on individual items are needed.

### Anatomy

#### Basic Implementation

```python
from nextpy.components.chakra.forms.iconbutton import IconButton
from nextpy.frontend.components.font_awesome.icon import FaIcon

# Create an IconButton with a specific icon
icon_button = IconButton.create(
    icon=FaIcon.create(name="fa-thumbs-up"),
    aria_label="Like",
    on_click=lambda: print("Liked!")
)
```

#### Advanced Implementation

```python
# Create an IconButton with additional properties and events
icon_button = IconButton.create(
    icon=FaIcon.create(name="fa-trash"),
    aria_label="Delete",
    is_round=True,
    is_disabled=Var(False),
    on_click=lambda: print("Item deleted"),
    style=Style(margin="10px", bg_color="red.500")
)
```

### Components

The `IconButton` component can be customized with the following properties:

| Prop Name    | Type                                      | Description                                                    |
|--------------|-------------------------------------------|----------------------------------------------------------------|
| type         | `Union[Var[str], str]`                    | The type of button (e.g., "submit", "reset").                  |
| aria_label   | `Union[Var[str], str]`                    | An accessibility label that describes the button.              |
| icon         | `Component`                               | The icon displayed on the button.                              |
| is_active    | `Union[Var[bool], bool]`                  | If `True`, styles the button in its active state.              |
| is_disabled  | `Union[Var[bool], bool]`                  | If `True`, the button will be disabled.                        |
| is_loading   | `Union[Var[bool], bool]`                  | If `True`, displays a spinner to indicate a loading state.     |
| is_round     | `Union[Var[bool], bool]`                  | If `True`, the button will be perfectly round.                 |
| spinner      | `Union[Var[str], str]`                    | The component used as a spinner when `is_loading` is `True`.   |
| as_          | `Union[Var[str], str]`                    | Overrides the default tag (e.g., `<button>`).                  |
| no_of_lines  | `Union[Var[int], int]`                    | Number of text lines after which to truncate and show ellipsis.|
| style        | `Style`                                   | The style object for custom styling.                           |
| ...          | `EventHandlers and additional properties` | Custom event handlers and additional properties.               |

### Notes

- Ensure the `aria_label` property is set for accessibility purposes, especially since the `IconButton` contains no text.
- When `is_loading` is `True`, the button will be disabled automatically.

### Best Practices

- Use clear and universally recognized icons to ensure the user understands the action associated with the `IconButton`.
- Avoid crowding the interface with too many `IconButton` components to maintain a clean and uncluttered UI.
- Implement appropriate event handlers such as `on_click` to provide interactive feedback to the user.
- Customize the button's appearance with the `style` property, but ensure it remains consistent with the overall design of the application.

By following these guidelines, you can create effective and user-friendly interfaces with the `IconButton` component in Nextpy.