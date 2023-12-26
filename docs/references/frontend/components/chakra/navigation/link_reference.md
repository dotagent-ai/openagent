##  Reference for nextpy/frontend/components/chakra/navigation/link.pyi

# Nextpy Documentation: Link Component

## Link

The `Link` component in the Nextpy library is used to create hyperlinks in your application. This component allows you to easily navigate between different pages or external resources while maintaining the application's state and ensuring smooth transitions.

### Use Cases

- Navigating to different routes within a single-page application (SPA).
- Linking to external websites or resources in a new tab.
- Creating navigation menus, breadcrumbs, and buttons with link-like behavior.

### Structure and Usage

The `Link` component is designed to work seamlessly with Nextpy's routing system, making it incredibly simple to create navigational elements in your app.

#### Anatomy

To use the `Link` component, you typically wrap text or other components with a `Link` to make them clickable. Here's a basic example:

```python
from nextpy.components.chakra.navigation import Link

# Simple text link
link = Link.create(href="/about", text="About Us")
```

To open a link in a new tab, you can set the `is_external` attribute to `True`:

```python
# External link
external_link = Link.create(href="https://example.com", text="Visit Example.com", is_external=True)
```

You can also use the `Link` component to wrap other components, such as an icon or an image:

```python
from nextpy.components.chakra.icon import Icon

# Icon link
icon_link = Link.create(href="/settings", children=[Icon.create(name="settings")])
```

#### Components

The `Link` component supports the following properties:

| Prop Name      | Type                                       | Description                                                |
|----------------|--------------------------------------------|------------------------------------------------------------|
| `children`     | `Component` or `Var[str]` or `str`         | The content to be displayed within the link.               |
| `rel`          | `str` or `Var[str]`                        | Specifies the relationship between the linked resource and the current document. Commonly used for SEO. |
| `href`         | `str` or `Var[str]`                        | The URL or route the link should navigate to.              |
| `text`         | `str` or `Var[str]`                        | The text to be displayed if `children` is not used.        |
| `as_`          | `str` or `Var[str]`                        | Defines the type of component to render as for custom routing. |
| `is_external`  | `bool` or `Var[bool]`                      | If `True`, the link will open in a new tab.                |
| `style`        | `Style`                                    | The CSS style to apply to the link.                        |
| `custom_attrs` | `Dict[str, Union[Var, str]]`               | Custom attributes for the link element.                    |
| `on_click`     | `EventHandler` or `EventSpec`              | Event handler for the click event.                         |

#### Event Triggers

The `Link` component supports several event handlers, such as:

- `on_click`
- `on_mouse_enter`
- `on_mouse_leave`
- `on_focus`
- `on_blur`

These events can be used to execute custom logic when the user interacts with the link.

### Notes

- Do not use the `Link` component for downloadable resources; instead, use a regular `<a>` tag with the `download` attribute.
- Make sure to provide meaningful text for links to ensure accessibility.

### Best Practices

- Use descriptive link text that indicates the link's purpose without needing additional context.
- Keep the `href` prop dynamic to accommodate variable routing paths.
- When linking to external sites, consider setting `rel="noopener noreferrer"` to improve security.

By following these guidelines and utilizing the `Link` component effectively, you can create a navigation experience that is both user-friendly and efficient.