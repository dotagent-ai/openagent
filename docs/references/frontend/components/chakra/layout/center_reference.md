##  Reference for nextpy/frontend/components/chakra/layout/center.pyi

# Nextpy Documentation: Center Component

## Center

### Overview

The `Center` component is a layout helper from Nextpy's Chakra UI that vertically and horizontally centers its child content within itself. It is a simple yet powerful tool for designing responsive and centered elements without the need for complex CSS or Flexbox properties.

### Purpose

The main purpose of the `Center` component is to provide a straightforward way to center content, such as text, images, or other components, in the middle of the available space. It is often used in situations where a piece of content or a component needs to be the focal point of a particular view or when creating a loading spinner or a placeholder.

### Use Cases

- Centering a logo or image on a splash screen.
- Displaying a loading spinner in the middle of the page while data is being fetched.
- Aligning a single button or a short message in the middle of a modal or pop-up.
- Creating a simple "Coming Soon" or "Under Maintenance" page with centered text.

### Structure

The `Center` component is a container that applies centering styles to its children. It should wrap around the content that needs to be centered.

### Usage

To use the `Center` component, you need to import it from the Nextpy library and then wrap it around the content you want to center.

```python
from nextpy.components.chakra.layout.center import Center

def main_view():
    centered_content = Center.create(
        "This content is centered!"
    )
    return centered_content
```

## Anatomy

### Basic Implementation

```python
# Basic usage to center text
centered_text = Center.create(
    "Centered Text Example"
)
```

### Advanced Implementation

```python
# Advanced usage with custom styles and additional properties
centered_box = Center.create(
    style=Style(width="50%", height="200px", background_color="gray.200"),
    custom_attrs={"data-testid": "centered-box"},
    on_click=lambda event: print("Box clicked!")
)(
    "Content within a custom styled Center box"
)
```

## Components

### Properties Table

| Prop Name       | Type       | Description                                                         |
|-----------------|------------|---------------------------------------------------------------------|
| children        | `*args`    | The content to be displayed inside the component.                    |
| style           | `Style`    | The style object that allows custom styling of the component.       |
| key             | `Any`      | A unique key that identifies the component.                         |
| id              | `Any`      | The identifier of the component.                                    |
| class_name      | `Any`      | The CSS class associated with the component.                        |
| autofocus       | `bool`     | Indicates whether the component should be focused on page load.     |
| custom_attrs    | `Dict`     | Custom HTML attributes to be applied to the component.              |
| on_blur         | `Event`    | Event handler triggered when the component loses focus.             |
| on_click        | `Event`    | Event handler triggered when the component is clicked.              |
| on_double_click | `Event`    | Event handler triggered on a double-click event on the component.   |
| on_focus        | `Event`    | Event handler triggered when the component gains focus.             |
| ...             | ...        | Additional event handlers and properties can be applied as needed.  |

### Event Triggers

- `on_click`: Triggered when the centered component is clicked.
- `on_focus`: Triggered when the component gains focus.
- `on_blur`: Triggered when the component loses focus.
- `on_mouse_enter`: Triggered when the mouse pointer enters the component.

## Notes

- The `Center` component is a convenience wrapper around CSS centering techniques and should not be used for complex layout structures.
- Child elements within `Center` will inherit the centering behavior; nested layouts may require additional consideration.

## Best Practices

- Use `Center` for single elements or small sets of content where centering is the primary layout requirement.
- Avoid using `Center` as a substitute for Flexbox or Grid when building complex layouts.
- Combine `Center` with other Chakra layout components like `Box`, `Flex`, and `Grid` for responsive design and alignment control.
- Keep the usage of custom attributes minimal to maintain clean code and avoid conflicts with native component behavior.

Remember, the above content is a template for your documentation. Tailor the explanations, code snippets, and best practices to match the specific features and behavior of your `Center` component.