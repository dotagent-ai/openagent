##  Reference for nextpy/frontend/components/chakra/datadisplay/keyboard_key.pyi

# Nextpy Documentation - KeyboardKey Component

## KeyboardKey

**Overview**: The `KeyboardKey` component visually represents a key from the keyboard. It is typically used to display keyboard shortcuts to the user.

**Purpose**: The primary use of `KeyboardKey` is to improve the user interface by providing a clear and recognizable visual cue for keyboard interactions within web applications.

**Use Cases**: 
- Displaying keyboard shortcuts in documentation or help sections.
- Enhancing tutorials that teach keyboard navigation or shortcuts.
- Creating interactive demos where users can learn and test keyboard shortcuts.

**Structure**: The `KeyboardKey` component is designed to look like a physical key on a keyboard, often with a box-like appearance and a monospaced font to represent the key character or label.

**Usage**:

```python
from nextpy.components.chakra.datadisplay import KeyboardKey

# Basic usage
key_component = KeyboardKey.create("Ctrl")

# With additional styling
styled_key = KeyboardKey.create("A", style=Style(bg="gray.200", padding="2"))
```

## Anatomy

The `KeyboardKey` component can be implemented with minimal parameters for a straightforward display or can be customized with additional attributes for more advanced scenarios.

### Basic Implementation

```python
# Basic Keyboard Key
key_component = KeyboardKey.create("Ctrl")
```

### Advanced Implementation

```python
# Advanced with additional properties and event handlers
advanced_key = KeyboardKey.create(
    "Enter",
    style=Style(border="2px solid black", borderRadius="md"),
    on_click=lambda event: print("Enter key clicked"),
)
```

## Components

### Sub-components

The `KeyboardKey` component is a standalone element and does not have sub-components.

### Properties Table

| Prop Name       | Type                                                        | Description                                                             |
|-----------------|-------------------------------------------------------------|-------------------------------------------------------------------------|
| `style`         | `Optional[Style]`                                           | Specifies the style of the component.                                   |
| `key`           | `Optional[Any]`                                             | A unique key for the component.                                         |
| `id`            | `Optional[Any]`                                             | The identifier for the component.                                       |
| `class_name`    | `Optional[Any]`                                             | The class name for the component.                                       |
| `autofocus`     | `Optional[bool]`                                            | Automatically focus the component when the page loads.                  |
| `custom_attrs`  | `Optional[Dict[str, Union[Var, str]]]`                      | Custom attributes for the component.                                    |
| `on_blur`       | `Optional[Union[EventHandler, EventSpec, list, function]]`  | Event handler for the blur event.                                       |
| `on_click`      | `Optional[Union[EventHandler, EventSpec, list, function]]`  | Event handler for the click event.                                      |
| `...`           | `...`                                                       | Additional event handlers for standard mouse and keyboard events.       |

### Event Triggers

The `KeyboardKey` component supports various event handlers for handling keyboard and mouse interactions.

## Notes

- Ensure that the key labels are clear and correspond accurately to actual keyboard keys for effective communication.
- Avoid using the `KeyboardKey` component to represent non-keyboard elements as this can confuse users.

## Best Practices

- Use the `KeyboardKey` component within the context where keyboard navigation or shortcuts are relevant.
- Keep the design consistent with the overall UI theme, but ensure that the keyboard keys stand out for easy identification.
- When displaying combinations of keys, space them with a plus symbol (`+`) for clarity, for example, `Ctrl + C`.
- Consider accessibility by providing alternative descriptions for keyboard interactions.