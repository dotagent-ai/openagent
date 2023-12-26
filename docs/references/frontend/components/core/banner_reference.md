##  Reference for nextpy/frontend/components/core/banner.pyi

As a Nextpy Documentation Writer, your task is to provide users with clear documentation for the `nextpy/components/core/banner.py` module. Here is an example documentation that reflects the structure and content needed for the `WebsocketTargetURL`, `ConnectionBanner`, and `ConnectionModal` components within this module.

---

# WebsocketTargetURL

## Overview

The `WebsocketTargetURL` component is used to specify a target URL for a websocket connection within a Nextpy application.

## Anatomy

### Basic Usage

To use the `WebsocketTargetURL` component, you can simply create an instance and provide the URL:

```python
from nextpy.components.core.banner import WebsocketTargetURL

websocket_url = WebsocketTargetURL.create(contents="wss://example.com/websocket")
```

### Advanced Usage

You can also specify additional properties such as style, custom attributes, and event handlers:

```python
from nextpy.components.core.banner import WebsocketTargetURL

websocket_url = WebsocketTargetURL.create(
    contents="wss://example.com/websocket",
    style=my_custom_style,
    on_click=my_click_handler
)
```

## Components

| Prop Name      | Type                                                      | Description                                                  |
| -------------- | --------------------------------------------------------- | ------------------------------------------------------------ |
| `contents`     | `Optional[Union[Var[str], str]]`                          | The URL to be used for establishing a websocket connection.  |
| `style`        | `Optional[Style]`                                         | The style object that defines the appearance of the component. |
| `custom_attrs` | `Optional[Dict[str, Union[Var, str]]]`                    | Custom attributes for the HTML element.                      |
| `on_click`     | `Optional[Union[EventHandler, EventSpec, list, function, BaseVar]]` | Event handler for the click event.                           |

## Notes

- Ensure the URL provided is valid and corresponds to a websocket server endpoint.
- The `contents` property is mandatory for establishing a connection.

## Best Practices

- Use secure `wss://` URLs for encrypted websocket connections.
- Handle connection errors gracefully by providing user feedback.

---

# ConnectionBanner

## Overview

The `ConnectionBanner` component is used to display a notification banner to the user when there is a server connection error.

## Anatomy

### Basic Usage

To use the `ConnectionBanner` component, create an instance:

```python
from nextpy.components.core.banner import ConnectionBanner

connection_banner = ConnectionBanner.create()
```

### Advanced Usage

You can provide a custom component to be rendered inside the banner:

```python
from nextpy.components.core.banner import ConnectionBanner, default_connection_error

connection_banner = ConnectionBanner.create(
    style=my_custom_style,
    children=default_connection_error()
)
```

## Components

| Prop Name      | Type                                                      | Description                                                  |
| -------------- | --------------------------------------------------------- | ------------------------------------------------------------ |
| `style`        | `Optional[Style]`                                         | The style object that defines the appearance of the banner.   |
| `custom_attrs` | `Optional[Dict[str, Union[Var, str]]]`                    | Custom attributes for the HTML element.                      |
| `children`     | `Optional[list[str | Var | Component]]`                   | The components to be rendered inside the banner.             |

## Notes

- The banner will be automatically displayed when there is a connection error, no additional setup is required.

## Best Practices

- Customize the appearance of the banner to match your application's theme.
- Provide clear and actionable messages to the user in case of connection errors.

---

# ConnectionModal

## Overview

The `ConnectionModal` component is used to display a modal dialog to the user when there is a server connection error.

## Anatomy

### Basic Usage

To use the `ConnectionModal` component, create an instance:

```python
from nextpy.components.core.banner import ConnectionModal

connection_modal = ConnectionModal.create()
```

### Advanced Usage

You can provide a custom component to be rendered inside the modal:

```python
from nextpy.components.core.banner import ConnectionModal, default_connection_error

connection_modal = ConnectionModal.create(
    style=my_custom_style,
    children=default_connection_error()
)
```

## Components

| Prop Name      | Type                                                      | Description                                                  |
| -------------- | --------------------------------------------------------- | ------------------------------------------------------------ |
| `style`        | `Optional[Style]`                                         | The style object that defines the appearance of the modal.   |
| `custom_attrs` | `Optional[Dict[str, Union[Var, str]]]`                    | Custom attributes for the HTML element.                      |
| `children`     | `Optional[list[str | Var | Component]]`                   | The components to be rendered inside the modal.              |

## Notes

- The modal will be automatically displayed when there is a connection error, no additional setup is required.

## Best Practices

- Customize the appearance of the modal to match your application's theme.
- Provide clear and actionable messages to the user in case of connection errors.

---

This documentation should guide users through using these components, their options, and best practices. It is important to maintain a consistent format throughout the documentation for clarity and ease of use.