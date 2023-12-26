##  Reference for nextpy/frontend/components/chakra/disclosure/accordion.pyi

# Nextpy Accordion Component Documentation

## Accordion

### Overview

The `Accordion` component allows you to display collapsible sections of content, also known as an accordion. It is particularly useful when you want to organize content into separate sections that a user can expand or collapse independently.

### Use Cases

- Frequently Asked Questions (FAQs)
- Product feature descriptions
- Organizing lengthy content into sections

### Anatomy

To use an `Accordion`, you will need to include the `Accordion`, `AccordionItem`, `AccordionButton`, and `AccordionPanel` components.

#### Basic Implementation

```python
from nextpy.components.chakra.disclosure import Accordion, AccordionItem, AccordionButton, AccordionPanel

accordion = Accordion.create(
    AccordionItem.create(
        AccordionButton.create("Section 1 title"),
        AccordionPanel.create("Section 1 content")
    ),
    AccordionItem.create(
        AccordionButton.create("Section 2 title"),
        AccordionPanel.create("Section 2 content")
    )
)
```

#### Advanced Implementation

```python
from nextpy.components.chakra.disclosure import Accordion, AccordionItem, AccordionButton, AccordionPanel
from nextpy.backend.vars import Var

allow_multiple = Var(False)

accordion = Accordion.create(
    items=[("Section 1", "Content 1"), ("Section 2", "Content 2")],
    allow_multiple=allow_multiple
)

# To programmatically change the `allow_multiple` property
allow_multiple.set(True)
```

### Components

#### Accordion

This is the main wrapper component that groups all `AccordionItem` components.

##### Properties

| Prop Name       | Type                         | Description                                       |
|-----------------|------------------------------|---------------------------------------------------|
| items           | `list of tuples (label,panel)`| List of tuples containing the label and panel content for each section. |
| icon_pos        | `Literal["right", "left"]`  | The position of the icon indicating expand/collapse action. |
| allow_multiple  | `Var[bool], bool`            | Determines whether multiple accordion items can be expanded simultaneously. |
| allow_toggle    | `Var[bool], bool`            | Allows collapsing the currently expanded item when clicked again. |
| default_index   | `Var[List[int]], List[int]`  | Index(es) of the initially expanded item(s).     |
| index           | `Var[int, List[int]], int, List[int]` | Controls the expanded item(s) programmatically. |
| reduce_motion   | `Var[bool], bool`            | Disables animations if set to True.               |
| ...             |                              | Inherited properties from `ChakraComponent`.      |

#### AccordionItem

Represents a single section within the accordion, containing a button and a panel.

##### Properties

| Prop Name       | Type                         | Description                                       |
|-----------------|------------------------------|---------------------------------------------------|
| id_             | `Var[str], str`              | A unique identifier for the accordion item.       |
| is_disabled     | `Var[bool], bool`            | If true, the accordion item will be disabled.     |
| is_focusable    | `Var[bool], bool`            | If true, the accordion item can receive focus.    |
| ...             |                              | Inherited properties from `ChakraComponent`.      |

#### AccordionButton

A button that controls the visibility of its corresponding `AccordionPanel`.

##### Properties

| Prop Name       | Type                         | Description                                       |
|-----------------|------------------------------|---------------------------------------------------|
| ...             |                              | Inherited properties from `ChakraComponent`.      |

#### AccordionPanel

The content area that is shown or hidden when the `AccordionButton` is activated.

##### Properties

| Prop Name       | Type                         | Description                                       |
|-----------------|------------------------------|---------------------------------------------------|
| ...             |                              | Inherited properties from `ChakraComponent`.      |

#### AccordionIcon

An optional icon that indicates the expand or collapse action, typically placed inside the `AccordionButton`.

##### Properties

| Prop Name       | Type                         | Description                                       |
|-----------------|------------------------------|---------------------------------------------------|
| ...             |                              | Inherited properties from `ChakraComponent`.      |

### Notes

- When using `allow_multiple`, make sure to also manage the `index` prop if you need to control the expanded sections programmatically.
- Consider accessibility best practices such as ensuring the accordion is navigable via keyboard.

### Best Practices

- Label each `AccordionButton` clearly to indicate what content it relates to.
- Use `default_index` or `index` to set which items are expanded by default or to control the expanded sections dynamically.
- Keep animations enabled unless necessary to reduce motion for accessibility reasons. Use `reduce_motion` as needed.
- Utilize `AccordionIcon` to provide a visual cue for the expand/collapse action.
- Test the accordion functionality across different screen sizes to ensure responsive behavior.

This documentation serves as a guide for developers to implement and customize the `Accordion` component within their Nextpy applications. It aims to provide clarity on the structure, usage, and customization options available.