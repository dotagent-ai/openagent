##  Reference for nextpy/frontend/components/chakra/forms/switch.pyi

# Switch Component

## Overview

The `Switch` component is a part of the Nextpy Chakra UI library and provides a user interface element that allows users to toggle between two states, typically denoted as "on" and "off". It functions similarly to a checkbox but offers a more intuitive and user-friendly interface for binary choices. The `Switch` is commonly used for settings that can be enabled or disabled, such as turning on/off notifications or switching between dark and light themes.

## Anatomy

The `Switch` component is composed of a track and a thumb. The track represents the background that the thumb slides over. The state of the switch is visually indicated by the position of the thumb and the color of the track.

**Basic Usage:**

```python
from nextpy.components.chakra.forms import Switch

# Create a basic switch
my_switch = Switch.create()
```

**Advanced Usage:**

```python
from nextpy.components.chakra.forms import Switch

# Create a switch with additional properties
my_advanced_switch = Switch.create(
    is_checked=True,
    color_scheme="green",
    is_disabled=False,
    on_change=lambda event: print("Switch state changed", event.is_checked)
)
```

## Components

The `Switch` component's properties include:

| Prop Name      | Type                    | Description                                                                    |
| -------------- | ----------------------- | ------------------------------------------------------------------------------ |
| `is_checked`   | `Optional[Union[Var[bool], bool]]` | Determines whether the switch is on (`True`) or off (`False`).                 |
| `is_disabled`  | `Optional[Union[Var[bool], bool]]` | If `True`, the switch will be non-interactive and greyed out.                  |
| `is_focusable` | `Optional[Union[Var[bool], bool]]` | If `True`, the switch can be focused even when disabled.                       |
| `is_invalid`   | `Optional[Union[Var[bool], bool]]` | If `True`, indicates the switch is in an error state.                          |
| `is_read_only` | `Optional[Union[Var[bool], bool]]` | If `True`, the switch is in read-only mode.                                    |
| `is_required`  | `Optional[Union[Var[bool], bool]]` | If `True`, the switch is required in a form context.                           |
| `name`         | `Optional[Union[Var[str], str]]`   | The name attribute of the switch input element.                                |
| `value`        | `Optional[Union[Var[str], str]]`   | The value attribute of the switch input element when it's checked.             |
| `spacing`      | `Optional[Union[Var[str], str]]`   | Space between the switch and its label text.                                   |
| `placeholder`  | `Optional[Union[Var[str], str]]`   | Placeholder text for the switch component.                                     |
| `color_scheme` | `Optional[Union[Var[LiteralColorScheme], LiteralColorScheme]]` | Color theme of the switch, affecting its appearance.                           |
| `style`        | `Optional[Style]`          | The CSS style of the switch component.                                         |
| `key`          | `Optional[Any]`            | Unique identifier for maintaining component state across re-renders.           |
| `id`           | `Optional[Any]`            | The ID attribute of the switch component.                                      |
| `class_name`   | `Optional[Any]`            | The class attribute of the switch component.                                   |
| `autofocus`    | `Optional[bool]`           | If `True`, the component will automatically focus on page load.                |
| `custom_attrs` | `Optional[Dict[str, Union[Var, str]]]` | Custom attributes for the switch component.                                   |
| `on_blur`      | `Optional[Union[EventHandler, EventSpec, list, function, BaseVar]]` | Event handler for when the component loses focus.                              |
| `on_change`    | `Optional[Union[EventHandler, EventSpec, list, function, BaseVar]]` | Event handler for when the switch's value changes.                             |
| `on_click`     | `Optional[Union[EventHandler, EventSpec, list, function, BaseVar]]` | Event handler for when the switch is clicked.                                  |
| ...            | ...                        | Other standard event handlers supported by HTML elements (e.g., `on_focus`, `on_mouse_enter`, etc.). |

## Notes

- When a `Switch` is set to `is_checked`, it becomes a controlled component. This means you must provide an `on_change` event handler to manage its state.
- The `value` property can hold any string, which is used when the switch is part of a form and is submitted.
- Custom styles can be applied to the `Switch` component using the `style` prop.

## Best Practices

- Use clear and concise labels for each switch to ensure users understand the option they are toggling.
- Avoid using switches for actions that have an immediate effect. They should be used for deferred changes that require a submit action.
- Keep the `color_scheme` consistent with the application's color palette for better user experience and accessibility.
- When using the switch in forms, always handle the `on_change` event to update the switch's state and potentially other parts of your UI.