##  Reference for nextpy/frontend/components/radix/primitives/accordion.pyi

# Nextpy Accordion Documentation

## Accordion

### Overview

An accordion is an interactive component that displays collapsible content panels for presenting information in a limited space. It is useful for FAQs, forms, and various other scenarios where space management is critical.

### Anatomy

Accordions generally consist of a set of items, each with a header and content area. Users can interact with the headers to show or hide the associated content.

#### Basic Usage:

```python
from nextpy.components.radix.primitives.accordion import AccordionRoot, AccordionItem, AccordionHeader, AccordionContent

accordion = AccordionRoot.create(
    AccordionItem.create(
        AccordionHeader.create("Section 1 Header"),
        AccordionContent.create("Section 1 Content")
    ),
    AccordionItem.create(
        AccordionHeader.create("Section 2 Header"),
        AccordionContent.create("Section 2 Content")
    )
)
```

#### Advanced Usage:

```python
accordion = AccordionRoot.create(
    type_="multiple",
    AccordionItem.create(
        value="item1",
        AccordionHeader.create("Section 1 Header"),
        AccordionContent.create("Section 1 Content")
    ),
    AccordionItem.create(
        value="item2",
        disabled=True,
        AccordionHeader.create("Section 2 Header"),
        AccordionContent.create("Section 2 Content")
    )
)
```

### Components

#### AccordionRoot

- **Purpose**: Root component for the accordion group.
- **Properties**:
    - `type_`: Accordion type—either `single` (only one panel open at a time) or `multiple` (multiple panels can be open).
    - `value`: The value of the currently expanded item.
    - `default_value`: The default value of the item to be expanded initially.
    - `collapsible`: If true, allows collapsing expanded items.
    - `disabled`: If true, disables user interaction with all accordion items.
    - `dir`: Text direction—either `ltr` (left-to-right) or `rtl` (right-to-left).
    - `orientation`: Orientation of the accordion—either `vertical` or `horizontal`.

#### AccordionItem

- **Purpose**: Represents a single accordion item.
- **Properties**:
    - `value`: A unique identifier for the item.
    - `disabled`: If true, disables interaction with this specific item.

#### AccordionHeader

- **Purpose**: The part of an accordion item that users can interact with to hide or show content.
- **Properties**: Inherits all properties from `AccordionComponent`.

#### AccordionContent

- **Purpose**: The content area of an accordion item that can be shown or hidden.
- **Properties**: Inherits all properties from `AccordionComponent`.

#### AccordionTrigger

- **Purpose**: An alternative to `AccordionHeader` for more control over the toggle element.
- **Properties**: Inherits all properties from `AccordionComponent`.

### Notes

- Ensure that each `AccordionItem` has a unique `value` when using the `type_="multiple"` to avoid unexpected behavior.
- Headers and content can contain any type of children, from simple text to complex components.

### Best Practices

- Use clear and concise headers to convey the purpose of each collapsible section.
- Avoid nesting accordions as it can lead to a confusing user experience.
- Consider accessibility by ensuring that the accordion works with keyboard navigation and screen readers.
- Use `type_="multiple"` sparingly as it can lead to an overwhelming experience if too many sections are open simultaneously.

This documentation is a brief overview of the Accordion component in Nextpy. For more detailed examples and advanced usage, developers are encouraged to refer to the full documentation on the official Nextpy website.