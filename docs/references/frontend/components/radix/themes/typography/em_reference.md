##  Reference for nextpy/frontend/components/radix/themes/typography/em.pyi

## `Em` Component

### Overview

The `Em` component is a typographic element that renders emphasized text, typically displayed as italicized by default. It is part of the Nextpy library's Radix theme components. This component is used to draw attention to certain text within a body of content or to denote a change in mood or voice.

### Anatomy

#### Basic Usage

```python
from nextpy.components.radix.themes.typography import Em

# Basic emphasized text
emphasized_text = Em.create("This text will be emphasized.")
```

#### Advanced Usage

```python
from nextpy.components.radix.themes.typography import Em
from nextpy.backend.vars import Var

# Advanced usage with dynamic variable and color scheme
dynamic_text = Var("Dynamic emphasized text")
emphasized_dynamic_text = Em.create(
    dynamic_text,
    color_scheme="purple",
    m="2"
)
```

### Components

The `Em` component has the following sub-components and properties:

#### Properties Table

| Prop Name          | Type                                                    | Description                                                                                               |
|--------------------|---------------------------------------------------------|-----------------------------------------------------------------------------------------------------------|
| color              | `Var[str]`, `str`                                       | Maps to the CSS default color property.                                                                    |
| color_scheme       | `Var[Literal[...]]`, `Literal[...]`                     | Maps to Radix color properties, providing predefined color schemes.                                        |
| access_key         | `Var[Union[str, int, bool]]`, `Union[str, int, bool]`   | Provides a keyboard shortcut hint for the element.                                                         |
| auto_capitalize    | `Var[Union[str, int, bool]]`, `Union[str, int, bool]`   | Controls text auto capitalization.                                                                         |
| content_editable   | `Var[Union[str, int, bool]]`, `Union[str, int, bool]`   | Indicates whether the element's content is editable.                                                       |
| ... (similar for other HTML attributes) | ...                                                     | ...                                                                                                       |
| m, mx, my, mt, mr, mb, ml | `Var[Literal["1"-"9"]]`, `Literal["1"-"9"]`         | Shorthand properties for setting margins.                                                                 |
| style              | `Style`                                                 | Allows for custom styling of the component.                                                               |
| key                | `Any`                                                   | A unique key for the component.                                                                            |
| id                 | `Any`                                                   | The id for the component.                                                                                  |
| class_name         | `Any`                                                   | The class name for the component.                                                                          |
| autofocus          | `bool`                                                  | If set, the component will take focus once the page loads.                                                 |
| custom_attrs       | `Dict[str, Union[Var, str]]`                            | Allows for custom attributes on the HTML element.                                                          |
| on_blur, on_click, and other event handlers | `EventHandler`, `EventSpec`, `list`, `function`, `BaseVar` | Event handlers for various user interactions and component lifecycle events. |

#### Event Triggers

- `on_blur`: Triggered when the component loses focus.
- `on_click`: Triggered when the component is clicked.
- `on_context_menu`: Triggered when the context menu is requested.
- ... (similar for other supported events)

### Notes

- The `Em` component should be used semantically to emphasize text that has stress emphasis, rather than for styling purposes.
- Custom attributes and styles should not conflict with the component's intended use and accessibility standards.

### Best Practices

- Use the `Em` component within the context of a sentence or phrase where emphasis is needed.
- Avoid overusing the `Em` component as it may reduce the impact of the emphasized text.
- Ensure that the color and size of the `Em` component is readable and accessible, especially when custom styles or color schemes are applied.
- When using dynamic content, ensure that the content updates are handled gracefully without causing layout shifts or user confusion.