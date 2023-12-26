##  Reference for nextpy/frontend/components/chakra/typography/heading.pyi

# Nextpy Documentation: `Heading` Component

## Heading

The `Heading` component in Nextpy provides an easy way to include styled text headings within your full-stack Python applications. Designed to integrate seamlessly with the Chakra UI design system, it allows developers to create typographic hierarchies and emphasize sections of content for both web and mobile interfaces.

### Use Cases

- Displaying the title of a page or a section.
- Creating visual hierarchy in text content.
- Highlighting important information.

### Structure and Usage

The `Heading` component is a wrapper around standard HTML heading tags, offering additional styling and functionality. By default, it renders as an `<h2>` tag but can be customized using the `as_` prop.

#### Basic Implementation

```python
from nextpy.components.chakra.typography import Heading

# Basic Heading with default size
heading_default = Heading.create("Welcome to Nextpy!")

# Heading with specified size
heading_large = Heading.create("Large Heading", size="lg")

# Custom tag usage, e.g., <h1>
custom_heading = Heading.create("Custom Tag Heading", as_="h1")
```

#### Advanced Implementation

```python
from nextpy.components.chakra.typography import Heading
from nextpy.frontend.style import Style

# Advanced Heading with custom style and size
advanced_heading = Heading.create(
    "Advanced Heading",
    size="2xl",
    style=Style(color="blue.500", bg="gray.100", padding="4", borderRadius="md")
)
```

### Components

The `Heading` component is standalone but can be nested with other components or elements to create complex structures.

#### Properties

| Prop Name      | Type                                                        | Description                                               |
| -------------- | ----------------------------------------------------------- | --------------------------------------------------------- |
| `as_`          | `Optional[Union[Var[str], str]]`                            | Overrides the default tag, e.g., `<h1>`, `<h3>`.          |
| `size`         | `Optional[Union[Var[LiteralHeadingSize], LiteralHeadingSize]]` | The size of the heading. Can be from `"xs"` to `"4xl"`.   |
| `style`        | `Optional[Style]`                                           | The CSS style of the component.                            |
| `key`          | `Optional[Any]`                                             | A unique key for the component.                            |
| `id`           | `Optional[Any]`                                             | The ID for the component.                                  |
| `class_name`   | `Optional[Any]`                                             | The class name for the component.                          |
| `autofocus`    | `Optional[bool]`                                            | Whether to focus the component on page load.               |
| `custom_attrs` | `Optional[Dict[str, Union[Var, str]]]`                      | Custom attributes for the component.                       |

#### Event Triggers

The `Heading` component can respond to various events such as clicks, focus changes, and mouse movements.

| Event Name         | Description                            |
| ------------------ | -------------------------------------- |
| `on_blur`          | Triggers when the component loses focus. |
| `on_click`         | Triggers when the component is clicked.  |
| `on_context_menu`  | Triggers on a right-click or context menu event. |
| `on_double_click`  | Triggers on a double-click event.         |
| `on_focus`         | Triggers when the component gains focus.  |
| ...                | Additional mouse and lifecycle events.    |

### Notes

- The `Heading` component inherits all native HTML attributes applicable to heading elements.
- When using the `style` prop, make sure to import `Style` from `nextpy.frontend.style`.

### Best Practices

- Use the `size` prop to maintain consistent typography scales across your application.
- Apply responsive styles by using the `Style` object properties.
- Always provide an `id` or `key` for headings that will be dynamically generated or repeated to maintain accessibility standards.

With the `Heading` component, developers have a powerful tool for crafting beautiful, accessible, and responsive text headings that enhance user interfaces and improve readability.