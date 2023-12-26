##  Reference for nextpy/frontend/components/chakra/forms/email.pyi

# Nextpy Documentation

## Email Component

### Overview

The `Email` component is a specialized form input that allows users to enter email addresses. It inherits from the `Input` component and includes all the base functionality of a text input, but it is specifically optimized for email input handling.

### Use Cases

- Capturing user email addresses for newsletters, sign-ups, and registration forms.
- Validating and submitting email data in a form.

### Anatomy

#### Basic Implementation

```python
from nextpy.components.chakra.forms.email import Email

email_input = Email.create(
    placeholder="Enter your email"
)
```

#### Advanced Implementation

```python
from nextpy.components.chakra.forms.email import Email
from nextpy.backend.vars import Var

email_value = Var('')

email_input = Email.create(
    value=email_value,
    placeholder="Enter your email",
    error_border_color="red.500",
    focus_border_color="green.500",
    is_required=True,
    on_change=lambda event: print(f"Email changed to: {event.target.value}")
)
```

### Components

- **Placeholder**: Provides guidance text within the input when it's empty.
- **Value**: A bindable `Var` or a static string reflecting the current email input.
- **Error Border Color**: The border color when the input is marked as invalid.
- **Focus Border Color**: The border color when the input has focus.
- **Disabled State**: Whether the input is interactable or not.
- **Invalid State**: Indicates the input has an error or invalid input.
- **Read-only State**: Makes the input uneditable but selectable.
- **Required State**: Marks the input as mandatory for form submission.

### Properties Table

| Prop Name          | Type                                        | Description                                                |
|--------------------|---------------------------------------------|------------------------------------------------------------|
| `type_`            | `Var[str]` or `str`                         | The type of input, should be set to 'email' by default.    |
| `value`            | `Var[str]` or `str`                         | The bound variable or the current value of the input.      |
| `default_value`    | `Var[str]` or `str`                         | The default value of the input.                            |
| `placeholder`      | `Var[str]` or `str`                         | The text that appears when the input is empty.             |
| `error_border_color` | `Var[str]` or `str`                      | Border color for the input when it is invalid.             |
| `focus_border_color` | `Var[str]` or `str`                      | Border color for the input when it is focused.             |
| `is_disabled`      | `Var[bool]` or `bool`                       | If true, the input is disabled.                            |
| `is_invalid`       | `Var[bool]` or `bool`                       | If true, the input is marked as invalid.                   |
| `is_read_only`     | `Var[bool]` or `bool`                       | If true, the input is read-only.                           |
| `is_required`      | `Var[bool]` or `bool`                       | If true, the input is required.                            |
| `variant`          | `Var[str]` or `str`                         | Style variant of the input.                                |
| `size`             | `Var[str]` or `str`                         | Size of the input.                                         |
| `name`             | `Var[str]` or `str`                         | The name of the input field.                               |
| `style`            | `Style`                                     | CSS style object for the component.                        |
| `key`              | `Any`                                       | A key that uniquely identifies the component.              |
| `id`               | `Any`                                       | The ID of the component.                                   |
| `class_name`       | `Any`                                       | The class attribute for the component.                     |
| `autofocus`        | `bool`                                      | Automatically focus the input when the page loads.         |
| `custom_attrs`     | `Dict[str, Union[Var, str]]`                | Custom attributes for the component.                       |
| `on_blur`          | `EventHandler` or `EventSpec`               | Event handler for the blur event.                          |
| `on_change`        | `EventHandler` or `EventSpec`               | Event handler for the change event.                        |
| `on_click`         | `EventHandler` or `EventSpec`               | Event handler for the click event.                         |
| ...                | ...                                         | ...                                                        |

### Notes

- The `type_` prop is predefined as 'email' and should not be modified.
- When binding a `Var` to the `value` property, any changes to the `Var` will be reflected in the input and vice versa.

### Best Practices

- Always use the `placeholder` property to provide a hint to the user about the expected email format.
- Bind a `Var` to the `value` property for reactive data handling and validation.
- Utilize the `is_required` property for form fields that must be filled.
- Use `error_border_color` and `is_invalid` to provide visual feedback on email validation.
- Attach event handlers like `on_change` to perform actions when the input value changes.

The `Email` component should be used whenever you need to collect email addresses from users. It streamlines form creation and ensures best practices for email input handling.