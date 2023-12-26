##  Reference for nextpy/frontend/components/gridjs/datatable.pyi

# Nextpy Documentation: `DataTable` Component

## Overview

The `DataTable` component in Nextpy is designed to create interactive and customizable data tables. It is a powerful tool for displaying tabular data with options for sorting, searching, pagination, and more. Ideal for dashboards, data analysis, and reporting interfaces, the `DataTable` component is flexible and easy to integrate into full-stack Python applications.

## Anatomy

### Basic Implementation

Here's a basic example of how to create a `DataTable` component using Nextpy:

```python
from nextpy.components.gridjs import DataTable

# Sample data
data = [
    ["John Doe", "john@example.com"],
    ["Jane Smith", "jane@example.com"]
]

# Corresponding column headers
columns = ["Name", "Email"]

# Create the DataTable component
data_table = DataTable.create(
    data=data,
    columns=columns
)
```

### Advanced Implementation

For more complex scenarios, you can enable features such as sorting, searching, and pagination:

```python
# Enabling search, sort, and pagination
data_table = DataTable.create(
    data=data,
    columns=columns,
    search=True,
    sort=True,
    pagination={
        'enabled': True,
        'limit': 10
    }
)
```

## Components

### Properties of the `DataTable` Component

| Prop Name   | Type                                          | Description                                                |
|-------------|-----------------------------------------------|------------------------------------------------------------|
| `data`      | `Optional[Any]`                               | The data to be displayed in the table.                     |
| `columns`   | `Optional[Union[Var[List], List]]`            | The column headers for the table.                          |
| `search`    | `Optional[Union[Var[bool], bool]]`            | Whether to enable a search bar.                            |
| `sort`      | `Optional[Union[Var[bool], bool]]`            | Whether to enable sorting on columns.                      |
| `resizable` | `Optional[Union[Var[bool], bool]]`            | Whether to allow column resizing.                          |
| `pagination`| `Optional[Union[Var[Union[bool, Dict]], ...]` | Enables pagination with optional configuration settings.   |
| ...         | ...                                           | Additional props inherited from `Gridjs` and `Component`.  |

### Event Handlers

The `DataTable` inherits event handlers from the `Component` class, allowing you to respond to various user interactions:

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

Each event handler can be set to a function that takes the event as an argument.

## Notes

- The `data` prop can accept a list of lists or a pandas DataFrame.
- Providing the `columns` prop is mandatory if `data` is a list of lists and must not be provided if `data` is a DataFrame.
- Custom styling can be applied to the `DataTable` using the `style` prop.

## Best Practices

- Define columns explicitly for clarity and control over column properties.
- Use pagination for large datasets to improve performance and usability.
- Always provide a unique `key` prop when rendering multiple instances to ensure proper component state management.
- Test the responsiveness of the `DataTable` in your application to ensure a good user experience across various screen sizes.

For more detailed examples and additional configuration options, refer to the complete `DataTable` API documentation and usage guides.