##  Reference for nextpy/frontend/components/chakra/forms/numberinput.pyi

# Nextpy Documentation: NumberInput Component

## NumberInput

### Overview

`NumberInput` is a component that allows users to enter numeric values. It provides functionality for incrementing and decrementing values, as well as direct text input. This component is suitable for scenarios where precise numeric values are required, such as setting a price, quantity, or other calculations.

### Use Cases

- Quantity selectors for e-commerce shopping carts
- Setting up thresholds or limits in a configuration panel
- Defining numerical parameters for data analysis tools
- Input fields in forms requiring numerical data

### Anatomy

The `NumberInput` component includes the following parts:

- **Input Field**: Where the user types the number.
- **Stepper Controls**: Increment (`NumberIncrementStepper`) and decrement (`NumberDecrementStepper`) buttons to change the value.

#### Basic Implementation

```python
from nextpy.components.chakra.forms import NumberInput

number_input = NumberInput.create(
    value=Var(10),
    min_=0,
    max_=100,
    step=1,
)

```

#### Advanced Implementation

```python
from nextpy.components.chakra.forms import NumberInput, NumberInputField, NumberInputStepper, NumberIncrementStepper, NumberDecrementStepper
from nextpy.backend.vars import Var

number_input_custom = NumberInput.create(
    NumberInputField.create(),
    NumberInputStepper.create(
        NumberIncrementStepper.create(),
        NumberDecrementStepper.create()
    ),
    value=Var(10),
    min_=0,
    max_=100,
    step=1,
    is_invalid=Var(False),
    error_border_color="red.500",
    focus_border_color="blue.500",
    on_change=lambda value: print("Value changed:", value)
)
```

### Components

#### `NumberInput`

| Prop Name               | Type                      | Description |
|-------------------------|---------------------------|-------------|
| `value`                 | `Var[Number]` \| `Number` | The current value of the number input. |
| `min_`                  | `Var[Number]` \| `Number` | The minimum value allowed. |
| `max_`                  | `Var[Number]` \| `Number` | The maximum value allowed. |
| `step`                  | `Var[Number]` \| `Number` | The step size for increment/decrement actions. |
| `variant`               | `LiteralInputVariant`     | The visual style of the number input. |
| `size`                  | `LiteralButtonSize`       | The size of the number input components. |
| `is_disabled`           | `Var[bool]` \| `bool`     | If `True`, the number input will be disabled. |
| `is_invalid`            | `Var[bool]` \| `bool`     | If `True`, indicates the input is invalid. |
| `is_read_only`          | `Var[bool]` \| `bool`     | If `True`, the input is read-only. |
| `is_required`           | `Var[bool]` \| `bool`     | If `True`, the input is required. |
| `allow_mouse_wheel`     | `Var[bool]` \| `bool`     | If `True`, allows changing the value by scrolling the mouse wheel. |
| `focus_input_on_change` | `Var[bool]` \| `bool`     | If `True`, focuses the input after value change via stepper. |

#### `NumberInputField`

Represents the text input field of the `NumberInput`. Accepts all common input props like `id`, `style`, `autofocus`, etc.

#### `NumberInputStepper`

Container for the increment and decrement stepper controls.

#### `NumberIncrementStepper` and `NumberDecrementStepper`

These are the buttons that increment or decrement the value. They accept common button props.

### Notes

- When using `NumberInput`, ensure that the `min_` and `max_` values are consistent with the expected range of inputs.
- The `value` should be a `Var` if you want to make it reactive and bind it to a state.

### Best Practices

- Use appropriate `variant` and `size` to match the design system of your application.
- Bind `value` to a `Var` if you want to monitor or control it programmatically.
- Provide `step` values that make sense for the context to ensure a good user experience.
- Utilize `allow_mouse_wheel` to enhance usability for mouse users, but consider disabling it when the input is not focused to prevent accidental value changes.
- Set `is_invalid` and provide `error_border_color` to give visual feedback when the input does not fulfill validation criteria.
- Always consider accessibility, such as labeling and ARIA attributes, to make the component usable for everyone.