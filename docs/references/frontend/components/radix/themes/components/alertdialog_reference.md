##  Reference for nextpy/frontend/components/radix/themes/components/alertdialog.pyi

# Nextpy Documentation: AlertDialog Component

## AlertDialog

### Overview

The AlertDialog component is designed to interrupt the user with important information that requires their attention before they can proceed. This component can be used to ensure users receive and acknowledge critical information before they continue with any other tasks within your application.

### Use Cases

- Confirmations before destructive actions, like deleting data.
- Warning users about potential risks or informing them about important updates.
- Displaying errors that need immediate user response.

### Structure

The AlertDialog is typically composed of several sub-components:

- **AlertDialogTrigger**: The element that triggers the dialog to open.
- **AlertDialogContent**: The container for the content of the dialog.
- **AlertDialogTitle**: The title of the dialog, which summarizes the purpose of the dialog.
- **AlertDialogDescription**: Additional descriptive text that provides more details to the user.

### Usage

Basic usage of the AlertDialog component involves importing the component and its sub-components, setting the `open` state, and defining the content within the dialog.

```python
from nextpy.components.radix.themes.components.alertdialog import (
    AlertDialog,
    AlertDialogTrigger,
    AlertDialogContent,
    AlertDialogTitle,
    AlertDialogDescription
)

# Define the open state for the AlertDialog
open_state = Var(False)

# Create AlertDialog with its sub-components
AlertDialog.create(
    AlertDialogTrigger.create(el.Button.create("Open Dialog")),
    AlertDialogContent.create(
        AlertDialogTitle.create("Confirmation"),
        AlertDialogDescription.create("Are you sure you want to proceed with this action?"),
        el.Button.create("Yes", on_click=lambda: open_state.set(False)),
        el.Button.create("No", on_click=lambda: open_state.set(False)),
        open=open_state
    )
)
```

### Anatomy

#### Basic Implementation

```python
# Basic AlertDialog component with minimal required properties
AlertDialog.create(
    AlertDialogTrigger.create(el.Button.create("Open Dialog")),
    AlertDialogContent.create(
        AlertDialogTitle.create("Important Alert"),
        AlertDialogDescription.create("This is an important message requiring your attention."),
        open=open_state
    )
)
```

#### Advanced Implementation

```python
# Advanced AlertDialog with additional properties and event handling
AlertDialog.create(
    AlertDialogTrigger.create(el.Button.create("Open Dialog", style={"color": "blue"})),
    AlertDialogContent.create(
        AlertDialogTitle.create("System Alert"),
        AlertDialogDescription.create("Your system will restart in 5 minutes to complete the update."),
        el.Button.create("Restart Now", on_click=handle_restart),
        el.Button.create("Cancel", on_click=handle_cancel),
        style={"backgroundColor": "lightgray"},
        on_open_change=handle_open_change,
        open=open_state
    )
)
```

### Components

#### AlertDialogTrigger

| Prop Name     | Type                            | Description                           |
|---------------|---------------------------------|---------------------------------------|
| *children     | Union[Var[str], str, Component] | The trigger element's display content |
| style         | Style                           | CSS styles for the trigger element    |
| on_click      | EventHandler                    | Event handler for click events        |

#### AlertDialogContent

| Prop Name      | Type                            | Description                                  |
|----------------|---------------------------------|----------------------------------------------|
| *children      | Union[Var[str], str, Component] | The content to display inside the dialog     |
| open           | Union[Var[bool], bool]          | The controlled open state of the dialog      |
| style          | Style                           | CSS styles for the content container         |
| on_open_change | EventHandler                    | Event handler for changes to the open state  |

#### AlertDialogTitle

| Prop Name  | Type                            | Description                   |
|------------|---------------------------------|-------------------------------|
| *children  | Union[Var[str], str, Component] | The title text of the dialog  |
| style      | Style                           | CSS styles for the title      |

#### AlertDialogDescription

| Prop Name  | Type                            | Description                       |
|------------|---------------------------------|-----------------------------------|
| *children  | Union[Var[str], str, Component] | The descriptive text of the dialog |
| style      | Style                           | CSS styles for the description   |

### Notes

- Always make sure to manage the `open` state properly to prevent the dialog from being stuck open or closed.
- Remember to provide accessible names and descriptions for screen reader users.

### Best Practices

- Use the AlertDialog sparingly and only for critical information. Overuse can lead to a frustrating user experience.
- Ensure that the dialog is modal and restricts interaction with the rest of the application until it is acknowledged.
- Provide clear and concise titles and descriptions within the dialog to communicate the information effectively.
- Include a clear action for the user to take, such as a confirmation or cancel button.