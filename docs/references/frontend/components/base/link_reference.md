##  Reference for nextpy/frontend/components/base/link.pyi

# Nextpy Documentation: RawLink Component

## RawLink

The `RawLink` component allows you to create hyperlinks in your Nextpy application. It's the basic building block for navigation and linking to external or internal resources.

### Anatomy

To use the `RawLink` component, you will generally need to specify the `href` attribute and any children (usually text or other components to display within the link). Below are examples of how to use the `RawLink` component.

#### Basic Implementation:

```python
from nextpy.components.base.link import RawLink

# Basic usage with a direct URL
link = RawLink.create(
    "Click me!",
    href="https://www.example.com"
)

# Usage with a variable for dynamic href
dynamic_href = Var("https://www.example.com")
link_with_var = RawLink.create(
    "Dynamic link",
    href=dynamic_href
)
```

#### Advanced Implementation:

```python
# Advanced usage with additional attributes and event handlers
advanced_link = RawLink.create(
    "Advanced Link",
    href=Var("https://www.example.com"),
    rel=Var("noopener noreferrer"),
    style=Style(color="blue", textDecoration="none"),
    on_click=lambda event: print("Link clicked!", event)
)
```

### Components

The `RawLink` component has several properties and events that you can use to customize its behavior.

#### Properties Table:

| Prop Name      | Type                                        | Description                                                   |
| -------------- | ------------------------------------------- | ------------------------------------------------------------- |
| `href`         | `Optional[Union[Var[str], str]]`            | The URL that the link points to.                               |
| `rel`          | `Optional[Union[Var[str], str]]`            | Specifies the relationship between the current document and the linked URL. Common values include `noopener` and `noreferrer`. |
| `style`        | `Optional[Style]`                           | The style object to apply custom styles to the link.           |
| `key`          | `Optional[Any]`                             | A unique key for the component in the context of its parent.   |
| `id`           | `Optional[Any]`                             | The HTML id attribute.                                        |
| `class_name`   | `Optional[Any]`                             | The HTML class attribute.                                     |
| `autofocus`    | `Optional[bool]`                            | If set to `True`, the component will automatically be focused when the page loads. |
| `custom_attrs` | `Optional[Dict[str, Union[Var, str]]]`      | Any custom attributes you want to add to the link element.    |

#### Event Triggers:

| Event Name         | Type                                                      | Description                                        |
| ------------------ | --------------------------------------------------------- | -------------------------------------------------- |
| `on_blur`          | `Optional[Union[EventHandler, EventSpec, list, function]]` | Called when the link loses focus.                  |
| `on_click`         | `Optional[Union[EventHandler, EventSpec, list, function]]` | Called when the link is clicked.                   |
| `on_context_menu`  | `Optional[Union[EventHandler, EventSpec, list, function]]` | Called when the context menu is requested on the link (right-click). |
| `on_double_click`  | `Optional[Union[EventHandler, EventSpec, list, function]]` | Called when the link is double-clicked.            |
| `on_focus`         | `Optional[Union[EventHandler, EventSpec, list, function]]` | Called when the link gains focus.                  |
| `on_mount`         | `Optional[Union[EventHandler, EventSpec, list, function]]` | Called when the link is mounted to the DOM.        |
| `on_mouse_down`    | `Optional[Union[EventHandler, EventSpec, list, function]]` | Called when a mouse button is pressed on the link. |
| ... (more events)  | ...                                                       | ...                                                |

### Notes

- Ensure that the `href` attribute is valid to avoid broken links.
- When using the `rel` attribute with the value `noopener noreferrer`, you enhance security and privacy by preventing the new page from being able to access the `window.opener` property and ensuring no referrer information is passed.
- Use the `style` property to adhere to your application's design system and maintain consistency across links.

### Best Practices

- **Accessibility**: Always include discernible text within your links to ensure accessibility for screen readers and other assistive technologies.
- **Security**: Use the `rel="noopener noreferrer"` attribute on links to external sites to increase security.
- **Performance**: Utilize event handlers like `on_click` to implement client-side navigation, which can improve the perceived performance of your application.
- **Custom Attributes**: Leverage `custom_attrs` for adding data attributes or non-standard attributes that might be required for CSS styling or JavaScript functionality.
- **Key Prop**: When rendering a list of links, always provide a unique `key` prop for each link to help Nextpy identify which items have changed, are added, or are removed. This can improve performance and prevent potential state issues.