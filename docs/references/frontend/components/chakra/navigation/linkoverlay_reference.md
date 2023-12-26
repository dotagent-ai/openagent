##  Reference for nextpy/frontend/components/chakra/navigation/linkoverlay.pyi

# LinkOverlay

## Overview

`LinkOverlay` is a component in the Nextpy library designed to provide a clickable overlay that can be used to navigate to different URLs or trigger actions within a full-stack Python application. This component is typically paired with `LinkBox` to create areas within your application that act as clickable regions, without the need to use traditional anchor tags (`<a>`).

## Anatomy

### Basic Usage

Here's a simple example of using `LinkOverlay`:

```python
from nextpy.components.chakra.navigation import LinkOverlay

link_overlay = LinkOverlay.create(
    "Click here to learn more",
    href=Var("https://example.com"),
    is_external=Var(True)
)
```

### Advanced Usage

```python
from nextpy.components.chakra.navigation import LinkOverlay
from nextpy.frontend.style import Style

# Styling the link overlay
custom_style = Style({
    "textDecoration": "underline",
    "color": "blue.500",
    "cursor": "pointer"
})

# Creating a LinkOverlay with custom styles and event handling
link_overlay = LinkOverlay.create(
    "Click for details",
    href=Var("/details"),
    style=custom_style,
    on_click=EventSpec(lambda event: print("Link clicked"))
)
```

## Components

The `LinkOverlay` component has the following properties:

| Prop Name     | Type                                | Description                                           |
|---------------|-------------------------------------|-------------------------------------------------------|
| `children`    | `*args`                             | The content of the link overlay, such as text or other components. |
| `is_external` | `Optional[Union[Var[bool], bool]]`  | If set to True, the link will open in a new tab.      |
| `href`        | `Optional[Union[Var[str], str]]`    | The URL that the link overlay points to.              |
| `style`       | `Optional[Style]`                   | The style properties to apply to the link overlay.    |
| `on_click`    | `Optional[Union[EventHandler, EventSpec, list, function, BaseVar]]` | The event handler for the click event. |

Event triggers like `on_click` are used to define behavior when the user interacts with the `LinkOverlay`.

## Notes

- Ensure that the `href` property is a valid URL when `is_external` is set to True.
- For internal navigation within a Nextpy application, use the `href` property without setting `is_external`.

## Best Practices

- Use `LinkOverlay` within a `LinkBox` to create larger clickable areas that are not restricted to text or icon boundaries.
- Style `LinkOverlay` appropriately to indicate it is clickable, for instance by changing the text color or adding underline on hover.
- Always provide meaningful text to `LinkOverlay` components for better accessibility.
- Consider using `on_click` event handlers for more complex interactions beyond simple navigation.