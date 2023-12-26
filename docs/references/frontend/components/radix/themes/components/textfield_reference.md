##  Reference for nextpy/frontend/components/radix/themes/components/textfield.pyi

# Nextpy `TextField` Component Documentation

## `TextFieldRoot`

### Overview
`TextFieldRoot` is a base component used to render a styled text field container. It includes common margin props and is designed to be used with specific `TextField` variants.

### Use Cases
`TextFieldRoot` can be used to provide a consistent look and feel for text fields across an application, in line with a chosen design system.

### Structure and Usage
`TextFieldRoot` creates a div element styled as a text field. It supports multiple properties for customization, such as color schemes, sizes, variants, radius, and margin properties.

### Anatomy
#### Basic Implementation
```python
# Create a TextFieldRoot with default properties
text_field_root = TextFieldRoot.create()
```
#### Advanced Implementation
```python
# Create a TextFieldRoot with custom properties
text_field_root = TextFieldRoot.create(
    color="blue",
    size="2",
    variant="surface",
    radius="medium",
    m="3"
)
```
### Components
#### Properties Table
| Prop Name          | Type                    | Description                                   |
|--------------------|-------------------------|-----------------------------------------------|
| color              | `Var[str]`, `str`       | The color of the text field.                  |
| color_scheme       | `Var[Literal]`, `Literal` | Predefined color schemes for the text field. |
| size               | `Var[LiteralTextFieldSize]`, `LiteralTextFieldSize` | Size of the text field: "1", "2", or "3".    |
| variant            | `Var[LiteralTextFieldVariant]`, `LiteralTextFieldVariant` | The variant of the text field: "classic", "surface", or "soft". |
| radius             | `Var[LiteralRadius]`, `LiteralRadius` | The border radius of the text field.         |
| ...                | ...                       | Additional HTML and custom attributes.       |

### Notes
- When setting properties that can take `Var` types, reactive behavior is enabled.

### Best Practices
- Use `color_scheme` to apply consistent branding across all text fields.
- Utilize `size` and `margin` props to align with your application's spacing and sizing system.

## `TextFieldInput`

### Overview
`TextFieldInput` is a component that renders an input element. It inherits from `TextFieldRoot` and includes additional input-specific properties.

### Use Cases
Utilize `TextFieldInput` whenever you need a user to input text, such as in forms, search bars, or login screens.

### Anatomy
#### Basic Implementation
```python
# Create a TextFieldInput with default properties
text_field_input = TextFieldInput.create()
```
#### Advanced Implementation
```python
# Create a TextFieldInput with custom properties
text_field_input = TextFieldInput.create(
    placeholder="Enter text here",
    variant="soft",
    radius="small",
    on_change=my_change_handler
)
```
### Components
#### Properties Table
| Prop Name          | Type                    | Description                                   |
|--------------------|-------------------------|-----------------------------------------------|
| accept             | `Var[str]`, `str`       | Accepted file types when input is of file type. |
| auto_complete      | `Var[str]`, `str`       | Specifies whether the input should have autocomplete enabled. |
| checked            | `Var[bool]`, `bool`     | Indicates whether the input is checked (checkboxes/radio). |
| disabled           | `Var[bool]`, `bool`     | Whether the input is disabled.                |
| max_length         | `Var[int]`, `int`       | The maximum number of characters allowed.     |
| pattern            | `Var[str]`, `str`       | The regex pattern for input validation.      |
| placeholder        | `Var[str]`, `str`       | The placeholder text for the input.          |
| required           | `Var[bool]`, `bool`     | Whether the input field is required.         |
| type               | `Var[str]`, `str`       | The type of input (e.g., text, email, password). |
| value              | `Var[str]`, `str`       | The value of the input field.                |
| ...                | ...                     | Additional properties from `TextFieldRoot`.   |

### Notes
- Avoid using `TextFieldInput` for non-textual data; instead, use appropriate input types (e.g., `date` for date pickers).

### Best Practices
- Use `placeholder` to provide guidance on what the user should enter.
- Employ `required`, `pattern`, and `max_length` for input validation.
- Handle `on_change` event to react to user input.

## `TextFieldSlot`

### Overview
`TextFieldSlot` is a component used to render additional elements alongside the `TextFieldInput`, such as icons or buttons.

### Use Cases
Use `TextFieldSlot` to enhance text fields with supplementary interactive elements or static decorations.

### Anatomy
#### Basic Implementation
```python
# Create a TextFieldSlot with default properties
text_field_slot = TextFieldSlot.create()
```
#### Advanced Implementation
```python
# Create a TextFieldSlot with an icon
text_field_slot = TextFieldSlot.create(
    color="gray",
    gap="2",
    children=[my_icon_component]
)
```
### Components
#### Properties Table
| Prop Name          | Type                    | Description                                   |
|--------------------|-------------------------|-----------------------------------------------|
| color              | `Var[str]`, `str`       | The color of the slot component.             |
| color_scheme       | `Var[Literal]`, `Literal` | Predefined color schemes for the slot.       |
| gap                | `Var[str]`, `str`       | The gap between the slot and input.          |
| ...                | ...                     | Additional HTML and custom attributes.       |

### Notes
- `TextFieldSlot` does not provide input functionality; it's meant for layout and decoration.

### Best Practices
- Keep the `gap` property consistent with the design system's spacing scale.
- Use `color_scheme` to maintain visual consistency with the `TextFieldInput`.

Remember to maintain clear and developer-friendly documentation throughout. Include explanations for all properties, and provide real-world examples to help developers understand how to use the `TextField` components effectively within their applications.