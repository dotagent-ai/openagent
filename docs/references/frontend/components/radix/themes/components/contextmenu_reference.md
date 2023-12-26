##  Reference for nextpy/frontend/components/radix/themes/components/contextmenu.pyi

# Nextpy's ContextMenu Component Documentation

## Overview

The `ContextMenu` component in Nextpy is used to create a context menu, which is a menu that appears upon user interaction, typically right-clicking on a given element or component. It allows developers to create interactive and accessible menus for their applications. 

## Anatomy

The `ContextMenu` consists of several sub-components that work together to provide a full context menu experience:

- `ContextMenuRoot`: The main container for the context menu.
- `ContextMenuTrigger`: The element that triggers the context menu to open.
- `ContextMenuContent`: The container for the menu items themselves.
- `ContextMenuSub`: A container for a nested submenu.
- `ContextMenuSubTrigger`: The element that triggers a submenu to open.
- `ContextMenuSubContent`: The container for submenu items.
- `ContextMenuItem`: A single item within a context menu.
- `ContextMenuSeparator`: A separator line used to group context menu items.

### Basic Usage

```python
from nextpy.components.radix.themes.components.contextmenu import (
    ContextMenuRoot, ContextMenuTrigger, ContextMenuContent,
    ContextMenuItem, ContextMenuSeparator
)

context_menu = ContextMenuRoot.create(
    ContextMenuTrigger.create('Right click me!'),
    ContextMenuContent.create(
        ContextMenuItem.create('Option 1'),
        ContextMenuItem.create('Option 2'),
        ContextMenuSeparator.create(),
        ContextMenuItem.create('Option 3'),
    )
)
```

### Advanced Usage

```python
# Advanced usage with submenus, event handling, and custom styling
context_menu_advanced = ContextMenuRoot.create(
    ContextMenuTrigger.create('Right click me!'),
    ContextMenuContent.create(
        ContextMenuItem.create('Option 1', on_click=handle_click_option1),
        ContextMenuSub.create(
            ContextMenuSubTrigger.create('Submenu'),
            ContextMenuSubContent.create(
                ContextMenuItem.create('Sub Option 1'),
                ContextMenuItem.create('Sub Option 2'),
            )
        ),
        ContextMenuSeparator.create(),
        ContextMenuItem.create('Option 3'),
    ),
    style=my_custom_style
)
```

## Components

### `ContextMenuRoot`

| Prop Name          | Type                     | Description                                                          |
|--------------------|--------------------------|----------------------------------------------------------------------|
| `children`         | `...`                    | Child components that make up the context menu.                      |
| `color`            | `Optional[Union[Var[str], str]]` | The text color of the component.                     |
| `color_scheme`     | `Optional[Union[Var[Literal[...]], Literal[...]]]` | The color scheme of the menu. |
| `modal`            | `Optional[Union[Var[bool], bool]]` | If `True`, the menu is modal and blocks interaction with other elements. |

### `ContextMenuTrigger`

| Prop Name          | Type                     | Description                                                          |
|--------------------|--------------------------|----------------------------------------------------------------------|
| `children`         | `...`                    | Child components that trigger the menu.                              |
| `color`            | `Optional[Union[Var[str], str]]` | The text color of the trigger.                     |
| `color_scheme`     | `Optional[Union[Var[Literal[...]], Literal[...]]]` | The color scheme of the trigger. |
| `disabled`         | `Optional[Union[Var[bool], bool]]` | If `True`, the trigger is disabled.                  |

### `ContextMenuContent`

| Prop Name          | Type                     | Description                                                          |
|--------------------|--------------------------|----------------------------------------------------------------------|
| `children`         | `...`                    | Child components that make up the menu content.                      |
| `color`            | `Optional[Union[Var[str], str]]` | The text color of the content.                     |
| `color_scheme`     | `Optional[Union[Var[Literal[...]], Literal[...]]]` | The color scheme of the content. |
| `size`             | `Optional[Union[Var[Literal["1", "2"]], Literal["1", "2"]]]` | The size of the content. |

### `ContextMenuSub`

(Similar to `ContextMenuRoot`)

### `ContextMenuSubTrigger`

(Similar to `ContextMenuTrigger`)

### `ContextMenuSubContent`

(Similar to `ContextMenuContent`, but for submenus)

### `ContextMenuItem`

| Prop Name          | Type                     | Description                                                          |
|--------------------|--------------------------|----------------------------------------------------------------------|
| `children`         | `...`                    | Child components that make up the menu item.                        |
| `color`            | `Optional[Union[Var[str], str]]` | The text color of the item.                          |
| `color_scheme`     | `Optional[Union[Var[Literal[...]], Literal[...]]]` | The color scheme of the item. |
| `shortcut`         | `Optional[Union[Var[str], str]]` | The shortcut key for the menu item.                  |

### `ContextMenuSeparator`

(Similar to `ContextMenuItem`, but renders as a separator)

## Notes

- It is important to handle events such as `on_click` for each `ContextMenuItem` to ensure that the menu performs actions when items are selected.
- The `color_scheme` prop accepts a specific set of color literals defined by Nextpy, which correspond to theme colors.

## Best Practices

- Use descriptive names for menu items to clearly communicate their action to the user.
- Avoid deep nesting of submenus to keep the context menu user-friendly.
- Consider accessibility by providing keyboard shortcuts and proper focus management.
- Use separators to group related items for better visual organization.
- Use `modal` judiciously, as it can impact the user experience by blocking interactions with other parts of the application.