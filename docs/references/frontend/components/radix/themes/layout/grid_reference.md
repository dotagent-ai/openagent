##  Reference for nextpy/frontend/components/radix/themes/layout/grid.pyi

# Nextpy Documentation: `Grid` Component

## Grid

The `Grid` component in Nextpy is a powerful and flexible way to create grid layouts within your full-stack Python applications. It is modeled after CSS Grid, with additional features from the Radix UI design system.

### Use Cases

- Building responsive web layouts with a grid-based structure.
- Aligning and distributing space among items within a container.
- Creating complex web designs without relying on traditional frameworks.

### Structure and Usage

The `Grid` component acts as a container that arranges its children in a grid layout. You can specify the number of columns and rows, as well as the alignment and justification of the grid items.

### Anatomy

The basic usage of the `Grid` component involves creating an instance of `Grid` and passing child elements to it:

```python
from nextpy.components.radix.themes.layout import Grid

grid = Grid.create(
    # Grid children go here
)
```

For advanced usage, you can customize the grid's appearance and behavior with various properties:

```python
grid = Grid.create(
    # Grid children,
    columns="3",
    rows="2",
    gap="4",
    align="center",
    justify="start",
    style=my_custom_style,
    # Other properties...
)
```

### Components

The `Grid` component has several sub-properties that can be used to customize its appearance and behavior:

| Prop Name        | Type                         | Description                                           |
|------------------|------------------------------|-------------------------------------------------------|
| color            | `str`, `Var[str]`            | Maps to the CSS default color property.               |
| color_scheme     | `str`, `Var[str]`            | Maps to Radix color property.                         |
| display          | `LiteralGridDisplay`, `Var`  | The display style of the grid.                        |
| columns          | `str`, `Var[str]`            | The number of columns in the grid.                    |
| rows             | `str`, `Var[str]`            | The number of rows in the grid.                       |
| flow             | `LiteralGridFlow`, `Var`     | The layout method for grid items.                     |
| align            | `LiteralAlign`, `Var`        | The alignment of children along the main axis.        |
| justify          | `LiteralJustify`, `Var`      | The alignment of children along the cross axis.       |
| gap              | `LiteralSize`, `Var`         | The gap between grid items.                           |
| gap_x            | `LiteralSize`, `Var`         | The horizontal gap between grid items.                |
| style            | `Style`                      | The style object for custom CSS styling.              |
| on_click         | `EventHandler`, `EventSpec`  | Event handler for click events on the grid.           |
| ...              | ...                          | Other global HTML attributes and event handlers.      |

### Notes

- When using `Var` for any property, you can bind the value dynamically, allowing the grid to react to state changes.
- Make sure to use the `gap` and `gap_x` properties responsibly to maintain a consistent layout across different screen sizes.

### Best Practices

- Use the `columns` and `rows` properties to define a grid template that fits your design requirements.
- Utilize `align` and `justify` to align grid items properly and create visually appealing layouts.
- When dealing with dynamic content, consider using `flow` to manage item placement automatically.
- Always test your grid layout on multiple screen sizes to ensure responsiveness.

In summary, the `Grid` component is a versatile tool in the Nextpy library that simplifies the creation of grid-based layouts in your applications. With its comprehensive set of properties and the ability to customize with `Style` and event handlers, you can create complex and responsive designs with ease.