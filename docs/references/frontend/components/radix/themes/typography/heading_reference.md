##  Reference for nextpy/frontend/components/radix/themes/typography/heading.pyi

# Heading Component

## Overview

The `Heading` component in the Nextpy library is used to create various levels of heading elements, typically resembling `<h1>` to `<h6>` tags in HTML. It is a customizable component that allows developers to set various typographic properties to suit their application's design needs.

## Use Cases

- Displaying section titles and subtitles in different sizes and weights.
- Organizing content hierarchy on a web page.
- Enhancing SEO by structuring content with semantic headings.

## Anatomy

### Basic Implementation

```python
from nextpy.components.radix.themes.typography.heading import Heading

# Basic usage
heading = Heading.create("Welcome to Nextpy!")
```

### Advanced Implementation

```python
from nextpy.components.radix.themes.typography.heading import Heading

# Advanced usage with properties
heading = Heading.create(
    "Advanced Heading",
    size="3",
    weight="bold",
    align="center",
    color="blue",
    m="4"
)
```

## Components

The `Heading` component can be customized with the following properties:

| Prop Name         | Type                      | Description                                         |
|-------------------|---------------------------|-----------------------------------------------------|
| `color`           | `str` or `Var[str]`       | Sets the text color.                                |
| `color_scheme`    | `Literal` or `Var`        | Sets the color scheme from predefined color palettes.|
| `as_child`        | `bool` or `Var[bool]`     | If true, replaces the component with the passed child. |
| `as_`             | `str` or `Var[str]`       | Changes the rendered element to a different tag.    |
| `size`            | `Literal` or `Var`        | The size of the heading from "1" to "9".            |
| `weight`          | `Literal` or `Var`        | The font weight: "light", "regular", "medium", "bold".|
| `align`           | `Literal` or `Var`        | The text alignment: "left", "center", "right".       |
| `trim`            | `Literal` or `Var`        | Trimming options for the text.                      |
| `high_contrast`   | `bool` or `Var[bool]`     | Whether to render text with higher contrast.        |
| ...               | ...                       | Other HTML attributes and event handlers.           |

## Notes

- The `size` prop corresponds to relative sizes, and it's internally mapped to the CSS font-size property.
- When using `as_child`, ensure that the child component is compatible and can accept the passed props.
- Ensure the `color_scheme` prop value matches one of the predefined color palettes.

## Best Practices

- Use headings in a descending order to maintain a proper content hierarchy for better readability and SEO.
- Keep the `size` prop relative to the importance of the heading within the content; for example, main titles should use larger sizes than subtitles.
- Avoid using too many different sizes and weights to maintain a clean and consistent design.
- Test color contrast, especially when using the `high_contrast` prop, to ensure readability for all users, including those with visual impairments.