##  Reference for nextpy/frontend/components/radix/themes/typography/code.pyi

# Code Component

## Overview

The `Code` component in Nextpy is designed to display inline code snippets or blocks of code within your application. It leverages the power of Nextpy's frontend capabilities along with Radix UI themes to provide a customizable and visually appealing code presentation component.

## Anatomy

### Basic Usage

Here's a simple example of how to use the `Code` component:

```python
from nextpy.components.radix.themes.typography import Code

# Using Code component to display an inline code snippet
code_snippet = Code.create("print('Hello, world!')")
```

### Advanced Usage

Below is an advanced example demonstrating various properties:

```python
from nextpy.components.radix.themes.typography import Code

# Advanced usage with color schemes, variant, size, and weight
code_block = Code.create(
    "def greet(name):\n\treturn f'Hello, {name}!'",
    color="black",
    color_scheme="gray",
    variant="solid",
    size="3",
    weight="bold",
    high_contrast=True
)
```

## Components

### Properties Table

| Prop Name         | Type                        | Description                                         |
|-------------------|-----------------------------|-----------------------------------------------------|
| color             | `Var[str]`, `str`           | CSS color property for the text.                    |
| color_scheme      | `Var[LiteralColor]`, `str`  | Radix color property, supports theme color tokens.  |
| variant           | `Var[LiteralVariant]`, `str`| Visual variant: "classic", "solid", "soft", etc.    |
| size              | `Var[LiteralTextSize]`, `str`| Text size, supports values "1" through "9".        |
| weight            | `Var[LiteralTextWeight]`, `str`| Text weight: "light", "regular", etc.            |
| high_contrast     | `Var[bool]`, `bool`         | Renders text with higher contrast if set to `True`. |
| ...               |                             | Additional HTML attributes and event handlers.      |

### Event Triggers

| Event Name      | Description                                 |
|-----------------|---------------------------------------------|
| on_click        | Triggered when the component is clicked.    |
| on_mouse_enter  | Triggered when the mouse enters the component area. |
| on_focus        | Triggered when the component gains focus.   |
| on_blur         | Triggered when the component loses focus.   |
| ...             | Other DOM-related events.                   |

## Notes

- The `Code` component should be used for code-related content only.
- Ensure that the color schemes used provide sufficient contrast for readability.
- Avoid using large code blocks with the `Code` component; for such cases consider using a dedicated code editor or viewer component.

## Best Practices

- When displaying code, use appropriate syntax highlighting where possible.
- Keep the code snippets concise and relevant to the context.
- Customize the `Code` component to match the overall theme and design language of your application.
- Use the `variant` property to provide visual distinction for different types of code snippets, such as comments, variables, or functions.
- Remember to test the responsiveness and accessibility of the component in different environments and screen sizes.