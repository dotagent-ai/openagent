##  Reference for nextpy/frontend/components/radix/themes/components/dropdownmenu.pyi

# Nextpy Dropdown Menu Component Documentation

## DropdownMenuRoot

### Overview

The `DropdownMenuRoot` component is the container for a dropdown menu. It wraps all other dropdown-related components and provides the context necessary for them to function together.

### Anatomy

To create a dropdown menu, use the `DropdownMenuRoot` to wrap around the trigger and content components.

#### Basic Implementation

```python
from nextpy.components.radix.themes.components.dropdownmenu import DropdownMenuRoot, DropdownMenuTrigger, DropdownMenuContent

root = DropdownMenuRoot.create(
    DropdownMenuTrigger.create('Options'),
    DropdownMenuContent.create(
        # Dropdown menu items go here
    )
)
```

#### Advanced Implementation

An advanced implementation might involve controlling the open state or customizing the dropdown's appearance.

```python
from nextpy.components.radix.themes.components.dropdownmenu import DropdownMenuRoot, DropdownMenuTrigger, DropdownMenuContent
from nextpy.backend.vars import Var

# Using Var to control the open state of the dropdown
open_state = Var(False)

root = DropdownMenuRoot.create(
    DropdownMenuTrigger.create('Options'),
    DropdownMenuContent.create(
        # Dropdown menu items go here
    ),
    open=open_state,
    on_open_change=lambda event: open_state.set(event.value)
)
```

### Components

#### DropdownMenuTrigger

This sub-component acts as the button or element that the user will interact with to toggle the dropdown menu's visibility.

Properties:
- `color`: Maps to CSS default color property.
- `color_scheme`: Maps to radix color property.

Events:
- `on_click`: Event triggered when the trigger is clicked.

#### DropdownMenuContent

This sub-component contains the actual dropdown menu items and can be styled accordingly.

Properties:
- `color`: Maps to CSS default color property.
- `color_scheme`: Maps to radix color property.

Events:
- `on_close_auto_focus`: Event that controls focus behavior when the dropdown menu is closed.
- `on_interact_outside`: Event triggered when there is an interaction outside of the dropdown menu content.

### Notes

- The `open` property in `DropdownMenuRoot` is controlled - you must provide `on_open_change` to handle its state changes.
- Avoid wrapping large parts of your application with `DropdownMenuRoot`, as it might affect performance and accessibility.

### Best Practices

- Use the `color` and `color_scheme` properties to ensure the dropdown menu fits the styling of your application.
- Handle state changes with care, particularly for the `open` state, to provide a smooth user experience.
- Use proper event handlers like `on_blur`, `on_focus`, and `on_interact_outside` to manage the dropdown's behavior in different scenarios.

## DropdownMenuTrigger

### Overview

`DropdownMenuTrigger` serves as the interactive element that users click to toggle the visibility of the dropdown menu.

### Anatomy

Wrap any element within `DropdownMenuTrigger` to make it the activator for the dropdown menu.

#### Basic Implementation

```python
from nextpy.components.radix.themes.components.dropdownmenu import DropdownMenuTrigger

trigger = DropdownMenuTrigger.create('Open Menu')
```

### Components

`DropdownMenuTrigger` does not have sub-components but works in tandem with `DropdownMenuRoot` and `DropdownMenuContent`.

### Notes

- `DropdownMenuTrigger` must be a direct child of `DropdownMenuRoot`.

### Best Practices

- Use text or icons that clearly indicate the purpose and action of the trigger to improve user experience.

## DropdownMenuContent

### Overview

`DropdownMenuContent` is the component that contains the items or contents of the dropdown menu.

### Anatomy

`DropdownMenuContent` typically contains a list of `DropdownMenuItem`, `DropdownMenuSubTrigger`, `DropdownMenuSubContent`, and `DropdownMenuSeparator`.

#### Basic Implementation

```python
from nextpy.components.radix.themes.components.dropdownmenu import DropdownMenuContent, DropdownMenuItem

content = DropdownMenuContent.create(
    DropdownMenuItem.create('Item 1'),
    DropdownMenuItem.create('Item 2'),
    # Additional items...
)
```

### Components

- `DropdownMenuItem`: Individual selectable items within the dropdown menu.
- `DropdownMenuSubTrigger` and `DropdownMenuSubContent`: For creating nested dropdown menus within a parent dropdown.
- `DropdownMenuSeparator`: A visual separator between groups of menu items.

### Notes

- Items within `DropdownMenuContent` should be direct children to ensure proper styling and functionality.

### Best Practices

- Group related items and use `DropdownMenuSeparator` to distinguish between different groups.

## DropdownMenuSubTrigger

### Overview

`DropdownMenuSubTrigger` functions like `DropdownMenuTrigger` but is used for creating nested dropdown menus within a parent dropdown menu.

### Anatomy

It's used in conjunction with `DropdownMenuSubContent` to create a hierarchy of menu items.

#### Basic Implementation

```python
from nextpy.components.radix.themes.components.dropdownmenu import DropdownMenuSubTrigger, DropdownMenuSubContent, DropdownMenuItem

sub_trigger = DropdownMenuSubTrigger.create(
    'Sub Menu',
    DropdownMenuSubContent.create(
        DropdownMenuItem.create('Sub Item 1'),
        DropdownMenuItem.create('Sub Item 2'),
        # Additional sub-items...
    )
)
```

### Components

Works with `DropdownMenuSubContent` to create submenus.

### Notes

- `DropdownMenuSubTrigger` must be a direct child of either `DropdownMenuContent` or another `DropdownMenuSubContent`.

### Best Practices

- Use clear labeling to indicate the presence of nested menus.

## DropdownMenuSubContent

### Overview

`DropdownMenuSubContent` contains the items for a nested dropdown menu.

### Anatomy

It should be used with `DropdownMenuSubTrigger` to create nested structures.

#### Basic Implementation

```python
from nextpy.components.radix.themes.components.dropdownmenu import DropdownMenuSubContent, DropdownMenuItem

sub_content = DropdownMenuSubContent.create(
    DropdownMenuItem.create('Sub Item 1'),
    DropdownMenuItem.create('Sub Item 2'),
    # Additional sub-items...
)
```

### Components

Contains `DropdownMenuItem` components for nested dropdowns.

### Notes

- `DropdownMenuSubContent` is used within `DropdownMenuSubTrigger`.

### Best Practices

- Keep nested menus straightforward and avoid deeply nested structures for better usability.

## DropdownMenuItem

### Overview

`DropdownMenuItem` represents a selectable item within a dropdown menu.

### Anatomy

Simple items that trigger actions when clicked.

#### Basic Implementation

```python
from nextpy.components.radix.themes.components.dropdownmenu import DropdownMenuItem

item = DropdownMenuItem.create('Item Label')
```

### Components

`DropdownMenuItem` is the fundamental interactive element within dropdown menus.

### Notes

- Can be used to perform actions or navigate to different parts of the application.

### Best Practices

- Use concise labels for menu items to make it easy for users to understand their purpose.

## DropdownMenuSeparator

### Overview

`DropdownMenuSeparator` is a non-interactive component that visually separates groups of menu items.

### Anatomy

A simple line or space used to distinguish between different sections of menu items.

#### Basic Implementation

```python
from nextpy.components.radix.themes.components.dropdownmenu import DropdownMenuSeparator

separator = DropdownMenuSeparator.create()
```

### Components

`DropdownMenuSeparator` is typically used between `DropdownMenuItem` components.

### Notes

- It is purely visual and does not contain any interactive elements.

### Best Practices

- Use sparingly to maintain a clean and organized dropdown menu structure.