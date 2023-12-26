##  Reference for nextpy/frontend/components/chakra/forms/select.pyi

# Nextpy `Select` Component Documentation

## Select

### Overview

The `Select` component in Nextpy is designed to offer developers a customizable and easy-to-use dropdown selection interface. It is similar to the traditional HTML `<select>` element but is enriched with additional styling and functionality provided by the Chakra UI design system.

### Purpose

`Select` is used to collect user input from a list of options. It is a form component that allows users to choose one item from a predefined list, making it ideal for scenarios where you want to present a controlled set of choices.

### Use Cases

- Replacing native dropdown menus in web forms.
- Enabling users to select from a list of options in a user-friendly manner.
- Collecting user preferences or choices as part of a form submission.

### Structure and Usage

The `Select` component is typically used within a form and can be bound to state variables for dynamic behavior. It comes with a set of properties that allow customization of its appearance, behavior, and accessibility features.

### Anatomy

#### Basic Implementation:

```python
select_value = Var("option1")

Select.create(
    Option.create("Option 1", value="option1"),
    Option.create("Option 2", value="option2"),
    Option.create("Option 3", value="option3"),
    value=select_value,
    placeholder="Select an option"
)
```

#### Advanced Implementation:

```python
select_value = Var("option2")

Select.create(
    Option.create("Option 1", value="option1"),
    Option.create("Option 2", value="option2"),
    Option.create("Option 3", value="option3"),
    value=select_value,
    placeholder="Select an option",
    size="lg",
    variant="filled",
    error_border_color="red.500",
    is_invalid=Var(False),
    on_change=handle_select_change
)
```

### Components

#### `Select` Properties

| Prop Name            | Type                                                  | Description                                                                           |
|----------------------|-------------------------------------------------------|---------------------------------------------------------------------------------------|
| value                | `Optional[Union[Var[str], str]]`                      | The bound variable containing the currently selected value.                           |
| default_value        | `Optional[Union[Var[str], str]]`                      | The initial value when the component is first rendered.                               |
| placeholder          | `Optional[Union[Var[str], str]]`                      | Placeholder text to display when no option is selected.                               |
| error_border_color   | `Optional[Union[Var[str], str]]`                      | The border color to use when the select is marked as invalid.                         |
| focus_border_color   | `Optional[Union[Var[str], str]]`                      | The border color to use when the select is focused.                                   |
| is_disabled          | `Optional[Union[Var[bool], bool]]`                    | If `True`, the select will be disabled and not interactable.                          |
| is_invalid           | `Optional[Union[Var[bool], bool]]`                    | If `True`, the select will be marked as invalid (e.g., for validation purposes).      |
| is_required          | `Optional[Union[Var[bool], bool]]`                    | If `True`, the select will be marked as required in a form context.                   |
| variant              | `Optional[LiteralInputVariant]`                       | The visual style variant of the select (e.g., "outline", "filled").                   |
| size                 | `Optional[Union[Var[str], str]]`                      | The size of the select component, affecting its height and text size.                 |
| name                 | `Optional[Union[Var[str], str]]`                      | The name attribute for the select, used in form submissions.                          |
| style                | `Optional[Style]`                                     | Custom styles to apply to the component.                                              |
| autofocus            | `Optional[bool]`                                      | If `True`, the select will automatically take focus when the page loads.              |
| custom_attrs         | `Optional[Dict[str, Union[Var, str]]]`                | Additional custom attributes for the select element.                                  |
| on_blur              | `Optional[EventHandler]`                              | Event handler for the blur event.                                                     |
| on_change            | `Optional[EventHandler]`                              | Event handler for the change event; called when an option is selected.                |

#### `Option` Properties

| Prop Name            | Type                                                  | Description                                                                           |
|----------------------|-------------------------------------------------------|---------------------------------------------------------------------------------------|
| value                | `Optional[Union[Var[Any], Any]]`                      | The value to be submitted when this option is selected.                               |
| as_                  | `Optional[Union[Var[str], str]]`                      | Override the HTML element to use for this component (defaults to `<option>`).         |
| style                | `Optional[Style]`                                     | Custom styles to apply to the component.                                              |

### Notes

- The `value` prop in `Select` should be a state variable (`Var`) if you intend to manage the selected value dynamically.
- Ensure that the `value` prop in `Option` components uniquely identifies the option.

### Best Practices

- Use meaningful labels for `Option` components to ensure user-friendliness.
- Apply appropriate sizing and variants to match the design system of your application.
- When using `Select` in forms, ensure to handle the `on_change` event to validate and store the selected value.
- Make use of `placeholder` to guide users when no default option is selected.
- Always include `is_required` when the field is mandatory for form submission to improve accessibility and user experience.