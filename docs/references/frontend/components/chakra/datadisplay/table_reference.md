##  Reference for nextpy/frontend/components/chakra/datadisplay/table.pyi

## Table

### Overview
The `Table` component in Nextpy is a versatile and customizable table display element inspired by Chakra UI, designed to present tabular data. 

### Use Cases
- Displaying structured data such as database contents, analytical data, or configuration settings.
- Creating sortable, filterable, and paginated tables for better data management in applications.

### Anatomy
The `Table` component can consist of various sub-components such as `Thead` (table header), `Tbody` (table body), `Tfoot` (table footer), `Tr` (table row), `Th` (table header cell), `Td` (table data cell), `TableCaption`, and `TableContainer`.

#### Basic Usage
```python
from nextpy.components.chakra.datadisplay import Table, Thead, Tbody, Tr, Th, Td

# Create a table with static data
table = Table.create(
    Thead.create(
        Tr.create(
            Th.create("Name"),
            Th.create("Age"),
            Th.create("Email")
        )
    ),
    Tbody.create(
        Tr.create(Td.create("John Doe"), Td.create("30"), Td.create("john@example.com")),
        Tr.create(Td.create("Jane Smith"), Td.create("25"), Td.create("jane@example.com"))
    )
)
```

#### Advanced Usage
```python
# Advanced table with dynamic data and styling
from nextpy.vars import Var
from nextpy.components.chakra.datadisplay import Table, Thead, Tbody, Tr, Th, Td

data = Var([
    {"name": "John Doe", "age": 30, "email": "john@example.com"},
    {"name": "Jane Smith", "age": 25, "email": "jane@example.com"}
])

table = Table.create(
    Thead.create(
        Tr.create(
            Th.create("Name"),
            Th.create("Age"),
            Th.create("Email")
        )
    ),
    Tbody.create(
        *[
            Tr.create(
                Td.create(item['name']),
                Td.create(str(item['age'])),
                Td.create(item['email'])
            ) for item in data.get()
        ]
    ),
    color_scheme="blue",
    variant="striped",
    size="md"
)
```

### Components
- **Thead**: Represents the header portion of the table.
- **Tbody**: Represents the body content of the table.
- **Tfoot**: Represents the footer portion of the table.
- **Tr**: Represents a row in the table.
- **Th**: Represents a header cell in the table which can have attributes like `is_numeric`.
- **Td**: Represents a data cell in the table which can have attributes like `is_numeric`.
- **TableCaption**: Provides a caption or title for the table.
- **TableContainer**: Wraps the table for additional styling or layout control.

### Notes
- Ensure that you provide a key when dynamically generating table rows or cells to optimize rendering.
- For accessibility, use `TableCaption` to describe the context of the table.

### Best Practices
- Use `variant`, `size`, and `color_scheme` props to style the table according to your application's theme.
- For a large amount of data, consider implementing pagination or virtualization to improve performance.
- When using dynamic data, always handle loading and error states gracefully.

This is a brief introduction to the `Table` components within the Nextpy library, providing you with the necessary details to start implementing tables in your Nextpy applications. For a comprehensive guide and more examples, refer to the full documentation.