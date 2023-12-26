##  Reference for nextpy/frontend/components/core/client_side_routing.pyi

# Nextpy Client-Side Routing Documentation

## ClientSideRouting

### Overview

The `ClientSideRouting` component in Nextpy is designed to handle navigation within a single-page application (SPA) without causing page reloads. This provides a smoother user experience by allowing dynamic content updates as the user interacts with the application.

### Use Cases

- Creating an SPA where different views are associated with distinct URLs.
- Implementing navigation menus that switch between content sections without server round-trips.
- Building dashboards or other applications with multiple user interface (UI) components that need to be shown or hidden based on the current route.

### Structure and Usage

The `ClientSideRouting` component works by listening to changes in the browser's URL and rendering the appropriate content based on the current route. It uses the HTML5 History API under the hood to manage navigation state without full page refreshes.

To use `ClientSideRouting`, you need to define routes and associate them with components that should be rendered when the route is matched.

### Anatomy

#### Basic Example

```python
from nextpy.components.core.client_side_routing import ClientSideRouting, Default404Page

app = ClientSideRouting.create(
    # Define your routes and associated components here
)

# Set a default route not found page
route_not_found.value = Default404Page.create()
```

#### Advanced Example

For a more advanced scenario, you might want to implement route parameters, guards, or nested routes. This would involve more complex configuration and potentially custom route matching logic.

### Components

#### Properties Table

Prop Name       | Type                                              | Description
--------------- | ------------------------------------------------- | --------------------------------------------------------------
`style`         | Optional[Style]                                   | Custom style to be applied to the routing container.
`key`           | Optional[Any]                                     | A unique key to identify the component instance.
`id`            | Optional[Any]                                     | The HTML id attribute.
`class_name`    | Optional[Any]                                     | CSS class name for styling.
`autofocus`     | Optional[bool]                                    | Automatically focus the component when it is loaded.
`custom_attrs`  | Optional[Dict[str, Union[Var, str]]]              | Custom HTML attributes for the component.
`on_blur`       | Optional[Union[EventHandler, EventSpec, list]]    | Event handler for blur events.
`on_click`      | Optional[Union[EventHandler, EventSpec, list]]    | Event handler for click events.
...             | ...                                               | Additional event handlers follow the same pattern.

#### Event Triggers

Event triggers are similar to the standard HTML event model and can be passed as props to respond to user actions or lifecycle events.

### Notes

- `ClientSideRouting` does not automatically handle scroll position restoration or data fetching for new routes. This logic must be implemented by the developer.
- `route_not_found` is a global `Var` that should be set to a component that will be rendered when no matching route is found.

### Best Practices

- Define routes using clear and consistent naming conventions.
- Use `route_not_found` to provide a user-friendly 404 error page.
- Keep the routing logic simple and avoid deeply nested routes for better maintainability.
- Consider code-splitting and lazy loading of components for routes to improve initial load performance.

By following these guidelines and structuring your documentation as shown, developers will find it easier to understand and implement client-side routing in their Nextpy applications.