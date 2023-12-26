##  Reference for nextpy/frontend/components/chakra/overlay/modal.pyi

# Nextpy Modal Documentation

## Modal

### Overview
The `Modal` component in Nextpy is a dialog overlay that is commonly used to capture user attention for critical information, decision making, or multi-step forms. It is also useful for preventing users from interacting with the rest of the application until they complete a specific task.

### Anatomy
The `Modal` component consists of several parts: `ModalOverlay`, `ModalContent`, `ModalHeader`, `ModalFooter`, `ModalBody`, and `ModalCloseButton`. Each part plays a role in the structure and presentation of the modal.

### Components

#### ModalOverlay
A transparent backdrop that covers the entire view when the modal is open, typically used to dim the background content.

#### ModalContent
The container for the modal's content. It includes the `ModalHeader`, `ModalBody`, and `ModalFooter`.

#### ModalHeader
The top part of the modal content that usually contains the title or heading of the modal.

#### ModalFooter
The bottom part of the modal content where actions like "Submit" or "Cancel" buttons are typically placed.

#### ModalBody
The middle section of the modal content where the main message or input fields are displayed.

#### ModalCloseButton
An optional close button typically placed in the upper right corner of the `ModalContent` to dismiss the modal.

### Usage

#### Basic Implementation
```python
from nextpy.components.chakra.overlay import Modal

modal = Modal.create(
    header="Modal Title",
    body="Modal content goes here",
    footer="Modal footer",
    is_open=True
)
```

#### Advanced Implementation with Event Triggers
```python
from nextpy.components.chakra.overlay import Modal
from nextpy.backend.vars import Var
from nextpy.backend.event import EventHandler

is_modal_open = Var(False)

def handle_modal_close(event):
    is_modal_open.set(False)

modal = Modal.create(
    header="Modal Title",
    body="Modal content goes here",
    footer="Modal footer",
    is_open=is_modal_open,
    on_close=EventHandler(handle_modal_close)
)
```

### Properties Table

| Prop Name                 | Type                                                | Description                                                                                     |
|---------------------------|-----------------------------------------------------|-------------------------------------------------------------------------------------------------|
| header                    | Optional[Union[Component, str]]                     | The header of the modal.                                                                        |
| body                      | Optional[Union[Component, str]]                     | The body of the modal.                                                                          |
| footer                    | Optional[Union[Component, str]]                     | The footer of the modal.                                                                        |
| close_button              | Optional[Component]                                 | The close button of the modal.                                                                  |
| is_open                   | Optional[Union[Var[bool], bool]]                    | If true, the modal will be open.                                                                |
| size                      | Optional[ModalSizes]                                | The size of the modal: "xs", "sm", "md", "lg", "xl", "full".                                    |
| ...                       | ...                                                 | Additional properties are available, matching the overloads provided in the stub file.           |

### Event Triggers

The `Modal` component can handle a variety of events:

| Event Name           | Description                                      |
|----------------------|--------------------------------------------------|
| on_blur              | Event triggered when the modal loses focus.      |
| on_click             | Event triggered when the modal is clicked.       |
| on_close             | Event triggered when the modal is requested to close. |
| on_close_complete    | Event triggered when the modal has finished closing. |
| on_esc               | Event triggered when the Esc key is pressed.     |
| on_overlay_click     | Event triggered when the modal overlay is clicked. |
| ...                  | Other events matching the overloads in the stub file. |

### Notes

- Ensure that the `Modal` component is used responsibly, as it can be intrusive if overused.
- The modal should be used for brief, focused tasks to avoid overwhelming users with too much information.

### Best Practices

- Use modals sparingly and only when necessary, as they interrupt the user's workflow.
- Keep the content concise and to the point to facilitate quick decision-making.
- Ensure that the modal is accessible, with appropriate focus management and keyboard navigation support.
- Customize the modal size appropriately based on the content, and ensure it is responsive across different screen sizes.

Remember to keep the documentation up to date with any changes to the Nextpy `Modal` component API, and provide examples that reflect common use cases to help developers understand how to use the component effectively in their applications.