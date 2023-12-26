##  Reference for nextpy/frontend/components/radix/themes/components/icons.pyi

# Nextpy Documentation: Radix Icon Component

## Overview

The Radix Icon Component is a part of the Nextpy library's UI components that allows developers to incorporate a variety of scalable icons into their full-stack Python applications. This component is tailored to provide a simple way to add visual elements that can enhance user interface design and user experience.

### Purpose

Icons serve as a visual representation of an action, idea, or concept, and can be used in buttons, menus, alerts, and more. They are essential in modern web design for intuitive navigation and for creating a more engaging and aesthetically pleasing application.

### Use Cases

- Enhancing buttons or interactive elements with visual cues.
- Displaying status indicators or notifications.
- Organizing content with visual hierarchy through different icons.
- Creating a visually consistent design language across an application.

### Structure and Usage

The Icon component is designed to be flexible and customizable, supporting various events and styles that can be tailored to fit the design requirements of a wide range of web applications.

## Anatomy

### Basic Implementation

```python
from nextpy.components.radix.themes.components.icons import Icon

# Creating a simple icon
home_icon = Icon.create(style={"fontSize": "24px"}, key="home-icon")
```

### Advanced Implementation

```python
from nextpy.components.radix.themes.components.icons import Icon
from nextpy.frontend.style import Style

# Creating an icon with additional styling and event handling
custom_icon_style = Style(color="blue", hover={"color": "red"}, fontSize="24px")
my_icon = Icon.create(
    style=custom_icon_style,
    on_click=lambda event: print("Icon clicked!"),
    key="custom-icon"
)
```

### Group Example

```python
from nextpy.components.radix.themes.components.icons import Icon, ICON_LIST
from nextpy.frontend.components.flex import Flex

# Displaying a set of icons
icon_set = Flex.create(
    *[
        Icon.create(style={"fontSize": "24px", "margin": "10px"}, key=f"icon-{name}")
        for name in ICON_LIST[:10]  # Displaying the first 10 icons from the list
    ],
    direction="row"
)
```

## Components

### Properties Table

| Prop Name      | Type                                                    | Description                                                            |
|----------------|---------------------------------------------------------|------------------------------------------------------------------------|
| style          | Optional[Style]                                         | Defines the CSS styles for the icon.                                   |
| key            | Optional[Any]                                           | A unique key for identifying the icon component.                       |
| id             | Optional[Any]                                           | The ID attribute for the icon element.                                 |
| class_name     | Optional[Any]                                           | The class attribute for the icon element.                              |
| autofocus      | Optional[bool]                                          | If set, the icon will take focus when the page loads.                  |
| custom_attrs   | Optional[Dict[str, Union[Var, str]]]                    | Allows setting custom attributes for the icon element.                 |
| on_blur        | Optional[Union[EventHandler, EventSpec, list, function]] | Event handler for the blur event.                                      |
| on_click       | Optional[Union[EventHandler, EventSpec, list, function]] | Event handler for the click event.                                     |
| ...            | ...                                                     | Other event handlers for various mouse and focus events follow a similar pattern. |

### Event Triggers

- `on_click`: Triggered when the icon is clicked.
- `on_mouse_enter`: Triggered when the cursor enters the icon area.
- `on_mouse_leave`: Triggered when the cursor leaves the icon area.
- Other mouse and focus events are also available and follow the same pattern.

## Notes

- Icons are purely decorative and do not include text, so it's important to provide proper accessibility features, such as `aria-label`, when necessary.
- Ensure that the icons used are consistent with the application's design language for a cohesive user experience.

## Best Practices

- Use icons sparingly and in meaningful ways to avoid clutter and confusion.
- Keep the size of icons consistent throughout the application unless different sizes serve a specific purpose.
- Customize the color and style of icons to match the application's theme.
- Provide appropriate alternative text or labels for icons to ensure accessibility.

This stub documentation provides a blueprint for expanding upon the Radix Icon Component's features and usage. It should be fleshed out with more specific examples, explanations, and guidance as the Nextpy library evolves.