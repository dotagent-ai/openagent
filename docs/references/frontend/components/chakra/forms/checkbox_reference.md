##  Reference for nextpy/frontend/components/chakra/forms/checkbox.pyi

# Checkbox Component

## Overview

The Checkbox component is an interactive element that allows users to select one or multiple options from a set. It's commonly used in forms and settings, enabling a binary choice, such as yes/no or true/false.

## Anatomy

### Basic Implementation

```python
from nextpy.components.chakra.forms.checkbox import Checkbox

# Creating a single checkbox
checkbox = Checkbox.create(
    "Subscribe to newsletter",
    is_checked=True
)
```

### Advanced Implementation

```python
from nextpy.components.chakra.forms.checkbox import Checkbox

# Creating a checkbox with additional properties
checkbox = Checkbox.create(
    "Accept Terms and Conditions",
    color_scheme='blue',
    size='md',
    is_disabled=False,
    on_change=handle_change
)

def handle_change(event):
    print("Checkbox state changed", event.target.is_checked)
```

## Components

### Properties

| Prop Name         | Type      | Description                                               |
| ----------------- | --------- | --------------------------------------------------------- |
| `color_scheme`    | `str`     | Defines the color scheme of the checkbox.                 |
| `size`            | `str`     | Sets the size of the checkbox (e.g., "sm", "md", "lg").   |
| `is_checked`      | `bool`    | Determines whether the checkbox is checked.               |
| `is_disabled`     | `bool`    | If `True`, the checkbox will be disabled.                 |
| `is_focusable`    | `bool`    | If `True`, the checkbox can be focused.                   |
| `is_indeterminate`| `bool`    | Renders the checkbox as indeterminate.                    |
| `is_invalid`      | `bool`    | Marks the checkbox as invalid for form validation.        |
| `is_read_only`    | `bool`    | If `True`, the checkbox will be read-only.                |
| `is_required`     | `bool`    | If `True`, the checkbox is required in a form context.    |
| `name`            | `str`     | Name attribute for the checkbox input.                    |
| `value`           | `str`     | The value to be used in the checkbox input.               |
| `spacing`         | `str`     | The space between the checkbox and its label.             |
| `style`           | `Style`   | A `Style` object to apply custom styles to the checkbox.  |

### Event Triggers

| Event Name     | Description                                  |
| -------------- | -------------------------------------------- |
| `on_change`    | Triggered when the checkbox state changes.   |
| `on_blur`      | Triggered when the checkbox loses focus.     |
| `on_focus`     | Triggered when the checkbox gains focus.     |
| `on_click`     | Triggered when the checkbox is clicked.      |

## Notes

- Avoid using `is_read_only` and `is_disabled` together as they can lead to a confusing user experience.
- The `is_indeterminate` state is visual only; it doesn't affect the actual checked state of the checkbox.

## Best Practices

- Use clear and concise labels for each checkbox.
- When creating a group of checkboxes, consider wrapping them in a `CheckboxGroup` for better accessibility.
- Be mindful of color schemes for contrast and readability.
- Use the `is_invalid` prop to visually indicate validation feedback.
- Provide ample spacing between checkboxes, especially when they are part of a form.