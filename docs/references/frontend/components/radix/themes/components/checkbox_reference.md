##  Reference for nextpy/frontend/components/radix/themes/components/checkbox.pyi

# Nextpy Checkbox Component Documentation

## Checkbox

### Overview

The `Checkbox` component is a standard UI element that allows users to make a selection from multiple options. Each checkbox operates independently, enabling the selection of zero, one, or multiple choices.

### Anatomy

The `Checkbox` component is constructed with various properties that allow customization of its appearance and behavior. Here is a basic implementation:

```python
from nextpy.components.radix.themes.components import Checkbox

checkbox = Checkbox.create(label="Subscribe to newsletter")
```

And here's an example with advanced features:

```python
from nextpy.components.radix.themes.components import Checkbox

checkbox = Checkbox.create(
    label="Accept Terms and Conditions",
    default_checked=True,
    disabled=False,
    size="2",
    variant="solid",
    color_scheme="blue",
    on_checked_change=my_checked_change_handler
)
```

### Components

- `label`: The text displayed next to the checkbox.
- `default_checked`: Sets the initial checked state of the checkbox.
- `checked`: Controls the checked state when used in controlled mode.
- `disabled`: Disables the checkbox if set to `True`.
- `size`: Adjusts the size of the checkbox. Accepts `"1"`, `"2"`, or `"3"`.
- `variant`: Defines the visual style. Options include `"classic"`, `"solid"`, `"soft"`, `"surface"`, `"outline"`, and `"ghost"`.
- `color_scheme`: Sets the color theme from predefined color options.
- `high_contrast`: If `True`, renders the checkbox with higher contrast.
- `radius`: Sets the border-radius of the checkbox, with options like `"none"`, `"small"`, `"medium"`, `"large"`, and `"full"`.
- `name`: The name attribute for the checkbox input element.
- `value`: The value attribute for the checkbox input element.

### Properties

| Prop Name         | Type                   | Description                                             |
|-------------------|------------------------|---------------------------------------------------------|
| `label`           | `str`                  | The text label for the checkbox.                        |
| `default_checked` | `bool`                 | Whether the checkbox is checked by default.             |
| `checked`         | `bool`                 | The controlled checked state.                           |
| `disabled`        | `bool`                 | If `True`, the checkbox is not interactive.             |
| `size`            | `LiteralCheckboxSize`  | The size of the checkbox.                               |
| `variant`         | `LiteralVariant`       | The visual style variant.                               |
| `color_scheme`    | `LiteralAccentColor`   | The color theme for the checkbox.                       |
| `high_contrast`   | `bool`                 | Enables higher contrast mode.                           |
| `radius`          | `LiteralRadius`        | The border-radius of the checkbox.                      |
| `name`            | `str`                  | The `name` attribute for the form input.                |
| `value`           | `str`                  | The `value` attribute for the form input.               |

### Event Triggers

- `on_checked_change`: Callback fired when the checkbox's checked state changes.
- `on_click`: Callback fired when the checkbox is clicked.
- `on_focus`: Callback fired when the checkbox gains focus.
- `on_blur`: Callback fired when the checkbox loses focus.

### Notes

- When using the `checked` property for controlled components, ensure that an `on_checked_change` handler is provided to update the state accordingly.
- The `default_checked` property is only used for uncontrolled components.

### Best Practices

- Use meaningful labels for accessibility and clarity.
- Group related checkboxes together visually.
- Use the `disabled` property sparingly to avoid confusion. Clearly indicate if an option is unavailable.
- For a set of options where multiple selections are not logical, consider using radio buttons instead.
- Avoid using too many variants within the same context to maintain UI consistency.

The above documentation provides a concise yet comprehensive guide to the `Checkbox` component within the Nextpy library. It covers the component's purpose, usage examples, properties, event triggers, important considerations, and best practices for effective use.