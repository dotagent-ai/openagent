##  Reference for nextpy/frontend/components/radix/themes/components/dialog.pyi

# Documentation for Nextpy's Dialog Components

The Dialog components in the Nextpy library provide a way to create modal dialog windows, which are useful for obtaining user input or displaying information in a focused manner without navigating away from the current page.

## DialogRoot

### Overview

The `DialogRoot` component serves as the container for the entire dialog. It controls the visibility and modality of the dialog window.

### Use Cases

- Displaying forms for user input, such as login or registration forms.
- Showing additional details about an item in a list.
- Confirming user actions, such as deleting a record.

### Anatomy

#### Basic Implementation

```python
from nextpy.components.radix.themes.components.dialog import DialogRoot

dialog = DialogRoot.create(
    # children components go here
    open=Var(True),  # Use a state variable to control the dialog's visibility
    modal=True  # Prevent interaction with the rest of the application
)
```

#### Advanced Implementation

```python
from nextpy.components.radix.themes.components.dialog import DialogRoot

dialog = DialogRoot.create(
    # children components go here
    open=Var(True),
    modal=True,
    style=Style(background_color="white", padding="20px"),
    on_open_change=lambda event: print("Dialog state changed", event)
)
```

### Components

#### Properties

| Prop Name      | Type                | Description                                                |
| -------------- | ------------------- | ---------------------------------------------------------- |
| color          | `Var[str]`, `str`   | Maps to CSS default color property.                        |
| color_scheme   | `Var[str]`, `str`   | Maps to radix color property.                              |
| open           | `Var[bool]`, `bool` | The controlled open state of the dialog.                   |
| modal          | `Var[bool]`, `bool` | When `True`, interaction outside the dialog will be disabled. |
| style          | `Style`             | The style of the component.                                |

#### Event Triggers

- `on_open_change`: Fired when the open state of the dialog changes.

### Best Practices

- Use `open` as a state variable to toggle the visibility of the dialog.
- Set `modal` to `True` to ensure the dialog captures focus and prevents interaction with the background elements.
- Always provide an accessible way to close the dialog, such as a close button or handling the escape key.

## DialogTrigger

### Overview

The `DialogTrigger` component is used to control the opening of its associated dialog.

### Use Cases

- A button that opens a dialog when clicked.
- An element that triggers a dialog to appear on a specific user interaction.

### Anatomy

#### Basic Implementation

```python
from nextpy.components.radix.themes.components.dialog import DialogTrigger

trigger = DialogTrigger.create(
    "Open Dialog",
    on_click=lambda: my_dialog_state.set(True)
)
```

#### Advanced Implementation

```python
from nextpy.components.radix.themes.components.dialog import DialogTrigger

trigger = DialogTrigger.create(
    "Open Dialog",
    style=Style(font_weight="bold"),
    on_click=lambda: my_dialog_state.set(True)
)
```

### Components

#### Properties

- Inherits common properties from `DialogRoot`.

### Best Practices

- Tie the `DialogTrigger` to the `open` state of the `DialogRoot` to ensure proper control over the dialog visibility.
- Clearly indicate the action the trigger will perform to improve user experience.

## DialogTitle

### Overview

The `DialogTitle` component is used for the title of the dialog, providing context about the dialog's content.

### Use Cases

- Displaying the title of a form within the dialog.
- Labeling the dialog for accessibility purposes.

### Anatomy

#### Basic Implementation

```python
from nextpy.components.radix.themes.components.dialog import DialogTitle

title = DialogTitle.create("Dialog Title")
```

### Components

#### Properties

- Inherits common properties from `DialogRoot`.

### Best Practices

- Always use `DialogTitle` for accessibility reasons, as it provides context for screen readers.

## DialogContent

### Overview

The `DialogContent` component is used to contain the main content of the dialog. It often holds forms, text, or other interactive elements.

### Use Cases

- Placing form fields for user input.
- Displaying messages or information to the user.

### Anatomy

#### Basic Implementation

```python
from nextpy.components.radix.themes.components.dialog import DialogContent

content = DialogContent.create(
    # content components go here
)
```

### Components

#### Properties

- Inherits common properties from `DialogRoot`.
- Additional HTML-related properties such as `role`, `spell_check`, etc.

### Best Practices

- Use `DialogContent` to wrap the main body of the dialog. It helps with accessibility and focus management.

## DialogDescription

### Overview

The `DialogDescription` component is used to provide additional descriptive text within the dialog.

### Use Cases

- Providing supplementary information about the dialog content.
- Offering instructions or help text to assist the user.

### Anatomy

#### Basic Implementation

```python
from nextpy.components.radix.themes.components.dialog import DialogDescription

description = DialogDescription.create("Additional information about the dialog.")
```

### Components

#### Properties

- Inherits common properties from `DialogRoot`.

### Best Practices

- Use `DialogDescription` to improve accessibility, particularly for users who rely on screen readers.

## DialogClose

### Overview

The `DialogClose` component is used to provide a closing mechanism for the dialog, such as a close button.

### Use Cases

- A close button typically represented with an "X" icon.
- An action button that dismisses the dialog.

### Anatomy

#### Basic Implementation

```python
from nextpy.components.radix.themes.components.dialog import DialogClose

close_button = DialogClose.create(
    "Close",
    on_click=lambda: my_dialog_state.set(False)
)
```

### Components

#### Properties

- Inherits common properties from `DialogRoot`.

### Best Practices

- Always provide a `DialogClose` component within your dialog to allow users to easily dismiss it.
- Ensure the close mechanism is clear and accessible to users of all abilities.

In conclusion, the Dialog components in Nextpy are designed to be flexible and accessible, providing developers with the building blocks to create a variety of dialog windows for their applications. When implementing these components, always consider best practices for usability and accessibility to provide a positive experience for all users.