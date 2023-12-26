##  Reference for nextpy/frontend/components/next/link.pyi

# Nextpy Documentation - NextLink Component

## NextLink

### Overview

The `NextLink` component is a fundamental part of the Nextpy library, designed to enable navigation between different pages or resources within a web application. It acts similarly to the `<a>` HTML tag in traditional web development, providing a clickable link that users can interact with to move to a new location or trigger an action.

### Use Cases

`NextLink` is commonly used for:

- Navigating between pages in a single-page application (SPA)
- Redirecting to external resources
- Creating hyperlinks within text or components
- Triggering actions when the link is clicked, such as opening a modal or executing a script

### Structure

`NextLink` is a component that can contain children, which are typically text or other inline components that represent the clickable area.

### Usage

To create a `NextLink` component, you use the `create` class method. Here's a basic example:

```python
from nextpy.components.next import NextLink

link = NextLink.create(
    "Click me!",
    href="/next-page",
    style={"color": "blue", "textDecoration": "none"}
)
```

In this example, "Click me!" is the clickable text, and clicking it will navigate the user to "/next-page".

## Anatomy

### Basic Implementation

```python
# Basic usage of NextLink with text
link = NextLink.create("Go to Home", href="/")

# With styling
styled_link = NextLink.create(
    "Go to Home",
    href="/",
    style=Style(color="blue", fontWeight="bold")
)
```

### Advanced Implementation

```python
# Advanced usage with events and custom attributes
advanced_link = NextLink.create(
    "Click me for more info",
    href="#",
    on_click=lambda event: print("Link clicked!"),
    custom_attrs={"data-info": "Additional info here"}
)
```

## Components

### Properties Table

| Prop Name      | Type                                              | Description                                                    |
| -------------- | ------------------------------------------------- | -------------------------------------------------------------- |
| `children`     | `Any`                                             | The children of the component.                                 |
| `href`         | `Optional[Union[Var[str], str]]`                  | The URL or route the link points to.                           |
| `pass_href`    | `Optional[Union[Var[bool], bool]]`                | Whether to pass the href prop to the child component.          |
| `style`        | `Optional[Style]`                                 | The CSS style applied to the component.                        |
| `key`          | `Optional[Any]`                                   | A unique key for the component.                                |
| `id`           | `Optional[Any]`                                   | The DOM id for the component.                                  |
| `class_name`   | `Optional[Any]`                                   | The class name for the component.                              |
| `autofocus`    | `Optional[bool]`                                  | Whether the component should focus on page load.               |
| `custom_attrs` | `Optional[Dict[str, Union[Var, str]]]`            | Custom attributes for the component's root element.            |

### Event Triggers

`NextLink` components can respond to a variety of events:

- `on_blur`
- `on_click`
- `on_context_menu`
- `on_double_click`
- `on_focus`
- `on_mount`
- `on_mouse_down`
- `on_mouse_enter`
- `on_mouse_leave`
- `on_mouse_move`
- `on_mouse_out`
- `on_mouse_over`
- `on_mouse_up`
- `on_scroll`
- `on_unmount`

Each event handler can be a function or an instance of `EventHandler` or `EventSpec`.

## Notes

- Ensure that the `href` property is set to a valid URL or route.
- Consider accessibility by providing descriptive text for screen readers.
- Do not overload the `NextLink` with too many children or complex components to maintain user-friendliness.

## Best Practices

- Use descriptive link text that indicates the action or destination.
- Keep styles consistent with your application's design language.
- Use `pass_href` judiciously, only when you need to pass the `href` to a child component.
- When using custom attributes, prefix them with `data-` to ensure HTML5 validity.
- Avoid using `NextLink` for actions that do not involve navigation; instead, use buttons or other interactive elements.