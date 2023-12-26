##  Reference for nextpy/frontend/components/glide_datagrid/dataeditor.pyi

# Nextpy DataEditor Component Documentation

## DataEditor

### Overview

The `DataEditor` component in Nextpy is a powerful and customizable data grid that allows developers to display, edit, and interact with tabular data in their web applications. It is designed to handle large datasets efficiently and provides a rich set of features such as sorting, filtering, data validation, and event handling.

### Purpose

The `DataEditor` component is primarily used to manage and present data in a spreadsheet-like interface. It enables users to perform CRUD (Create, Read, Update, Delete) operations on data and is suitable for applications such as administrative dashboards, data analysis tools, and any scenario where tabular data needs to be manipulated by users.

### Use Cases

- Displaying a list of records from a database with the ability to edit values inline.
- Providing a data analysis tool where users can sort, filter, and aggregate data.
- Creating an interface for managing inventory, orders, or customer data.

### Anatomy

#### Basic Implementation

```python
from nextpy.components.datadisplay.dataeditor import DataEditor

data_editor = DataEditor.create(
    columns=[{"title": "Name"}, {"title": "Age"}],
    data=[["Alice", 30], ["Bob", 25]],
    row_markers="number"
)
```

#### Advanced Implementation

```python
from nextpy.components.datadisplay.dataeditor import DataEditor, DataEditorTheme

custom_theme = DataEditorTheme(
    accent_color="#FF5733",
    text_header="#FFFFFF",
    bg_header="#333333"
)

data_editor = DataEditor.create(
    columns=[{"title": "Name"}, {"title": "Age"}],
    data=[["Alice", 30], ["Bob", 25]],
    theme=custom_theme,
    row_markers="number",
    on_cell_edited=lambda cell: print(f"Cell edited: {cell}")
)
```

### Components

#### `GridColumnIcons`

An enumeration defining the icons that can be used in the grid columns.

| Prop Name    | Type   | Description                                             |
|--------------|--------|---------------------------------------------------------|
| Array        | Enum   | Icon for an array column.                               |
| AudioUri     | Enum   | Icon for a column containing audio URIs.                |
| ...          | Enum   | ...                                                     |

... (Describe each Enum member similarly)

#### `DataEditorTheme`

A class defining the theme properties for the data editor.

| Prop Name               | Type        | Description                                     |
|-------------------------|-------------|-------------------------------------------------|
| accent_color            | str, Optional | Color for accent elements.                     |
| accent_fg               | str, Optional | Foreground color for accent elements.          |
| ...                     | ...         | ...                                             |

... (Describe each theme property similarly)

#### `DataEditor`

The main component for rendering a data grid.

| Prop Name               | Type                              | Description                                     |
|-------------------------|-----------------------------------|-------------------------------------------------|
| rows                    | Optional[Union[Var[int], int]]    | Number of rows in the data grid.                |
| columns                 | Optional[Union[Var[List[Dict[str, Any]]], List[Dict[str, Any]]]] | Column headers.        |
| ...                     | ...                               | ...                                             |

... (Describe each prop in detail)

### Notes

- The `DataEditor` component relies on the `NoSSRComponent` base class, indicating that it is rendered client-side and is not suitable for server-side rendering (SSR).
- Event handling props such as `on_cell_edited` should be provided with callable functions that match the expected signature.

### Best Practices

- Utilize `DataEditorTheme` to create a cohesive visual style that aligns with your application's branding.
- When handling large datasets, consider implementing pagination or virtualization to improve performance.
- Ensure that the provided event handlers manage state changes correctly to prevent unintended side effects.
- Use the `row_markers` property wisely to enhance usability, especially when displaying data that requires row selection or numbering.

This documentation is a starting point for integrating and utilizing the `DataEditor` component in Nextpy applications. Developers should refer to the provided code snippets and detailed component properties to create a data grid that meets their specific requirements.