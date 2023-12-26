##  Reference for nextpy/frontend/components/radix/themes/components/popover.pyi

# Nextpy Popover Component Documentation

## Popover

The `Popover` component is a non-modal dialog that floats around a trigger, typically used for displaying additional information or providing more user interactions without leaving the context of the page. It is commonly used to create dropdown menus, tooltips, and more. 

### Anatomy

**PopoverRoot**: This is the wrapper component that encapsulates the trigger and the content of the popover. It controls the open state and manages the popover visibility.

**PopoverTrigger**: The element that the popover is anchored to. When interacted with, it controls the visibility of the popover content.

**PopoverContent**: This is the actual content that is displayed in the popover.

**PopoverClose**: A component that can be used inside the `PopoverContent` to close the popover when clicked.

#### Basic Implementation

```python
from nextpy.components.radix.themes.components.popover import PopoverRoot, PopoverTrigger, PopoverContent, PopoverClose

popover = PopoverRoot.create(
    PopoverTrigger.create(Button.create("Click me")),
    PopoverContent.create(
        Text.create("Popover content goes here."),
        PopoverClose.create(Button.create("Close"))
    )
)
```

#### Advanced Implementation

```python
from nextpy.components.radix.themes.components.popover import PopoverRoot, PopoverTrigger, PopoverContent, PopoverClose

popover_with_customization = PopoverRoot.create(
    PopoverTrigger.create(Button.create("Click me")),
    PopoverContent.create(
        Text.create("Customized popover content."),
        PopoverClose.create(Button.create("Close")),
        side="bottom",
        align="start",
        avoid_collisions=True,
        side_offset=10,
        color_scheme="blue",
        modal=True
    ),
    open=True  # Controlled open state
)
```

### Components

#### PopoverRoot

| Prop Name       | Type                                                         | Description                                                                                                                                 |
|-----------------|--------------------------------------------------------------|---------------------------------------------------------------------------------------------------------------------------------------------|
| color           | `Var[str]`, `str`                                            | Maps to CSS default color property.                                                                                                         |
| color_scheme    | `Var[Literal[...]]`, `Literal[...]`                          | Maps to radix color property.                                                                                                               |
| open            | `Var[bool]`, `bool`                                          | The controlled open state of the popover.                                                                                                   |
| modal           | `Var[bool]`, `bool`                                          | The modality of the popover. Interaction with outside elements is disabled and only popover content is visible to screen readers when true. |
| ...             | ...                                                          | ...                                                                                                                                         |

#### PopoverTrigger

| Prop Name       | Type                                                         | Description                         |
|-----------------|--------------------------------------------------------------|-------------------------------------|
| color           | `Var[str]`, `str`                                            | Maps to CSS default color property. |
| color_scheme    | `Var[Literal[...]]`, `Literal[...]`                          | Maps to radix color property.       |
| ...             | ...                                                          | ...                                 |

#### PopoverContent

| Prop Name           | Type                                                         | Description                                                                                                                                              |
|---------------------|--------------------------------------------------------------|----------------------------------------------------------------------------------------------------------------------------------------------------------|
| color               | `Var[str]`, `str`                                            | Maps to CSS default color property.                                                                                                                      |
| color_scheme        | `Var[Literal[...]]`, `Literal[...]`                          | Maps to radix color property.                                                                                                                            |
| size                | `Var[Literal[1, 2, 3, 4]]`, `Literal[1, 2, 3, 4]`            | Size of the popover content.                                                                                                                             |
| side                | `Var[Literal["top", "right", "bottom", "left"]]`, `Literal[...]` | The preferred side of the anchor to render against when open.                                                                                             |
| side_offset         | `Var[int]`, `int`                                            | The distance in pixels from the anchor.                                                                                                                  |
| align               | `Var[Literal["start", "center", "end"]]`, `Literal[...]`     | The preferred alignment against the anchor.                                                                                                              |
| align_offset        | `Var[int]`, `int`                                            | The vertical distance in pixels from the anchor.                                                                                                         |
| avoid_collisions    | `Var[bool]`, `bool`                                          | When true, overrides the side and align preferences to prevent collisions with boundary edges.                                                           |
| ...                 | ...                                                          | ...                                                                                                                                                      |

#### PopoverClose

| Prop Name       | Type                                                         | Description                         |
|-----------------|--------------------------------------------------------------|-------------------------------------|
| color           | `Var[str]`, `str`                                            | Maps to CSS default color property. |
| color_scheme    | `Var[Literal[...]]`, `Literal[...]`                          | Maps to radix color property.       |
| ...             | ...                                                          | ...                                 |

### Notes

- The `PopoverRoot` component must wrap both the `PopoverTrigger` and the `PopoverContent` components for proper functionality.
- To control the popover's visibility, use the `open` prop of the `PopoverRoot`.
- Use `PopoverClose` within `PopoverContent` to provide a close button.

### Best Practices

- Ensure that the popover content is accessible and does not trap keyboard focus.
- Avoid overly complex structures within the popover content; keep it concise and to the point.
- When modal is set to `true`, make sure that focus is managed correctly within the popover content to prevent focus from escaping to the underlying page.
- Use `side` and `align` props to control the popover's position relative to the trigger but be cautious of collisions with the viewport edges. The `avoid_collisions` prop can help with automatic adjustments.
- Consider the z-index of the popover if stacking context issues arise in your application design.