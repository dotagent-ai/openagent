##  Reference for nextpy/frontend/components/radix/themes/components/iconbutton.pyi

# IconButton

## Overview

The `IconButton` is a graphical button component typically used to trigger an action or event. It contains an icon instead of text, which makes it a preferred choice for toolbars, navigation menus, and form actions where space is at a premium or where visual cues are beneficial.

## Use Cases

- Toolbars and action items in user interfaces where icons can quickly communicate function.
- As a compact alternative to text-based buttons within forms or dialogs.
- In mobile applications or responsive designs where space is limited.
- For social media sharing buttons, settings toggles, or multimedia controls.

## Anatomy

### Basic Usage

```python
from nextpy.components.radix.themes.components.iconbutton import IconButton

# Creating a simple IconButton
icon_button = IconButton.create(
    # Icon can be a child component or an element like an SVG or an image
    children=[Icon(...)],
    on_click=lambda event: print("Button clicked!"),
    variant="ghost",
    size="2",
    color_scheme="blue"
)
```

### Advanced Usage

```python
# Advanced usage with additional properties
icon_button = IconButton.create(
    children=[Icon(...)],
    on_click=lambda event: handle_click(event),
    size="3",
    variant="solid",
    color_scheme="teal",
    high_contrast=True,
    radius="full",
    disabled=False,
    style=Style(...),
    custom_attrs={"data-attribute": "value"}
)
```

## Components

- **children**: The icons or elements to be displayed within the button.
- **on_click**: The event handler for the click event.
- **size**: Sets the size of the button, options: `"1"`, `"2"`, `"3"`, `"4"`.
- **variant**: The visual style of the button, options: `"solid"`, `"soft"`, `"outline"`, `"ghost"`.
- **color_scheme**: The color theme for the button, various options available.
- **high_contrast**: Boolean indicating if the button should have high contrast.
- **radius**: The border-radius of the button, options: `"none"`, `"small"`, `"medium"`, `"large"`, `"full"`.
- **disabled**: Boolean indicating if the button is disabled.
- **style**: An instance of `Style` for additional CSS styling.
- **custom_attrs**: A dictionary of custom attributes to be added to the button element.

## Notes

- Make sure the icon used inside the `IconButton` is visually clear and understandable.
- When `disabled` is set to `True`, the button will be non-interactive and visually indicate its disabled state.

## Best Practices

- Use `IconButton` for actions that are well represented by icons and are recognizable to users.
- Avoid using too many icon buttons in close proximity to prevent user confusion.
- Provide an `aria-label` or similar attribute when the icon's action is not obvious to assist screen readers and improve accessibility.
- Consider the button size and ensure it is large enough to be easily tapped on touch devices.
- When using `IconButton` in forms, ensure it is associated with the correct form element and behaves as expected upon submission.