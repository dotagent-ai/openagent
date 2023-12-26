##  Reference for nextpy/frontend/components/chakra/overlay/tooltip.pyi

# Tooltip Component Documentation

## Overview

The `Tooltip` component provides a small pop-up box that appears when the user moves the mouse cursor over an element. It is used to display additional information about an element similar to a tooltip you'd find in a typical desktop graphical user interface.

## Purpose and Use Cases

Tooltips are useful for providing brief context or feedback. They can explain functions of buttons or provide additional information that might help users without cluttering the UI. They can also be used to display form validation messages or additional details on images and links.

## Anatomy

A basic tooltip can be created with the `label` property, which defines the text shown inside the tooltip. Additional properties like `placement`, `has_arrow`, and `is_disabled` can be used to adjust its behavior and appearance.

### Basic Implementation:

```python
from nextpy.components.chakra import Tooltip

tooltip = Tooltip.create(
    label="More Info",
    children="Hover over me"
)
```

### Advanced Implementation:

```python
tooltip_advanced = Tooltip.create(
    label="Detailed Information",
    children="Hover over me",
    has_arrow=True,
    placement="right",
    open_delay=500,  # Tooltip will be shown after a delay of 500ms
    close_on_click=True
)
```

## Components

Each `Tooltip` component may include the following properties:

| Prop Name              | Type                              | Description |
|------------------------|-----------------------------------|-------------|
| arrow_padding          | `Optional[Union[Var[int], int]]`  | Padding to prevent the arrow from reaching the edge of the popper. |
| arrow_shadow_color     | `Optional[Union[Var[str], str]]`  | Color of the arrow shadow. |
| arrow_size             | `Optional[Union[Var[int], int]]`  | Size of the arrow. |
| delay                  | `Optional[Union[Var[int], int]]`  | Delay before hiding the tooltip. |
| close_on_click         | `Optional[Union[Var[bool], bool]]`| Hide the tooltip on click. |
| close_on_esc           | `Optional[Union[Var[bool], bool]]`| Hide the tooltip when pressing the Esc key. |
| close_on_mouse_down    | `Optional[Union[Var[bool], bool]]`| Hide the tooltip while the mouse is down. |
| default_is_open        | `Optional[Union[Var[bool], bool]]`| Show the tooltip by default. |
| direction              | `Optional[Union[Var[Literal["ltr", "rtl"]], Literal["ltr", "rtl"]]]` | Direction for the theme (ltr or rtl). |
| gutter                 | `Optional[Union[Var[int], int]]`  | Margin between the reference and popper. |
| has_arrow              | `Optional[Union[Var[bool], bool]]`| Show an arrow tip. |
| is_disabled            | `Optional[Union[Var[bool], bool]]`| Disable the tooltip. |
| is_open                | `Optional[Union[Var[bool], bool]]`| Control the tooltip's visibility. |
| label                  | `Optional[Union[Var[str], str]]`  | The text shown in the tooltip. |
| open_delay             | `Optional[Union[Var[int], int]]`  | Delay before showing the tooltip. |
| placement              | `Optional[Union[Var[str], str]]`  | Placement of the tooltip relative to its reference. |
| should_wrap_children   | `Optional[Union[Var[bool], bool]]`| Wrap children in a span with `tabIndex=0`. |

## Notes

- The `label` property is required for the tooltip to display text.
- If `has_arrow` is `True`, the tooltip will display with an arrow pointing to the element.
- The `is_disabled` property can be used to disable the tooltip functionality without removing it from the DOM.

## Best Practices

- Use tooltips sparingly and only when necessary to avoid overwhelming the user with information.
- Keep tooltip text concise. If more detailed information is needed, consider using a different UI element.
- Test tooltip behavior at different screen sizes to ensure they do not obstruct important content.
- Make sure that the tooltip content is accessible to all users, including those using screen readers or keyboard navigation.