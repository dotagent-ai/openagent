##  Reference for nextpy/frontend/components/radix/themes/components/tooltip.pyi

# Nextpy Documentation

## Tooltip

### Overview

The `Tooltip` component in Nextpy provides a small pop-up box that appears when the user moves the cursor over an element or when the element is focused. Tooltips are used to display brief, contextual information about the function of an element on the page, typically used to inform users about the behavior of buttons, links, or form fields.

### Use Cases

- Displaying explanations for buttons on a toolbar.
- Offering instant help or additional information for form fields.
- Showing the full text of items that are too long to display in a table or list.

### Anatomy

The `Tooltip` component can be created with a range of properties that determine its appearance and behavior. Here's how to implement a basic tooltip:

```python
from nextpy.components.radix.themes.components import Tooltip

my_tooltip = Tooltip.create(
    content="This is a tooltip",
    color_scheme="blue",
    m="2"
)
```

#### Advanced Usage

For a more complex scenario, you might want to customize the tooltip's style or respond to events:

```python
my_advanced_tooltip = Tooltip.create(
    content="Detailed information here",
    color_scheme="green",
    on_mouse_enter=lambda: print("Hovering over the tooltip!"),
    style=Style(padding="10px", fontSize="14px")
)
```

### Components

The `Tooltip` inherits all the properties from `CommonMarginProps` and `RadixThemesComponent`, but also includes its specific properties:

| Prop Name      | Type    | Description                                                    |
|----------------|---------|----------------------------------------------------------------|
| `content`      | `str`   | The text or content to be displayed in the tooltip.            |
| `color`        | `str`   | Maps to the CSS default `color` property.                      |
| `color_scheme` | `str`   | Maps to the Radix color property, defining the color theme.    |
| `...`          | `...`   | Inherits margin and other styling props from parent components |

### Notes

- The `Tooltip` component should be used judiciously; too many tooltips on a page can lead to a cluttered interface and a confusing user experience.
- The `content` prop is required to display the tooltip.
- Tooltips are not typically used for touch devices, where hovering is not possible.

### Best Practices

- Keep the content concise and informative.
- Match the `color_scheme` with the element or the surrounding UI for a cohesive look.
- Ensure that the tooltip does not obstruct important UI elements.
- Do not use tooltips for critical information that users must read to use the application effectively.
- Test the tooltip's behavior on different devices and screen sizes to ensure usability.

Please remember that this is just a starting point for the documentation. As the library evolves, additional properties and events may be added, and the documentation should be updated accordingly. Furthermore, real-world examples and interactive demos greatly enhance the understanding and applicability of the documentation.