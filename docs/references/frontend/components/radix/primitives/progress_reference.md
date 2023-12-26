##  Reference for nextpy/frontend/components/radix/primitives/progress.pyi

# Progress Components

The Progress components in Nextpy are designed to visually represent the progress of an operation or task to the users. This documentation covers the use and customization of the Progress components, including `ProgressRoot` and `ProgressIndicator`.

## ProgressRoot

### Overview

`ProgressRoot` represents the container for a progress bar, defining the overall progress range and appearance.

### Anatomy

Here is a basic example of how to use `ProgressRoot`:

```python
from nextpy.components.radix.primitives.progress import progress_root

# Create a progress bar with a max value of 100 and a current value of 50
progress_bar = progress_root(value=50, max=100)
```

### Components

#### Properties

| Prop Name    | Type                           | Description                                      |
|--------------|--------------------------------|--------------------------------------------------|
| `value`      | `Optional[Union[Var[int], int]]` | The current value of the progress.              |
| `max`        | `Optional[Union[Var[int], int]]` | The maximum value of the progress.              |
| `style`      | `Optional[Style]`              | The style applied to the progress bar container. |
| `class_name` | `Optional[Any]`                | The class name for custom CSS styling.          |

#### Event Triggers

| Event Name     | Description                                     |
|----------------|-------------------------------------------------|
| `on_mount`     | Triggered when the component is mounted.        |
| `on_unmount`   | Triggered when the component is unmounted.      |
| `on_blur`      | Triggered when the component loses focus.       |
| `on_focus`     | Triggered when the component gains focus.       |
| `on_click`     | Triggered when the component is clicked.        |
| ...            | Other DOM event handlers.                       |

### Best Practices

- Use `ProgressRoot` to wrap one or more `ProgressIndicator` components to create a complete progress bar.
- Always provide a `max` value to define the scale of the progress.
- Use `value` to update the progress dynamically.

## ProgressIndicator

### Overview

`ProgressIndicator` is the visual representation of progress within the `ProgressRoot`. It shows the part of the progress bar that is filled based on the current value.

### Anatomy

Here is a basic example of how to use `ProgressIndicator`:

```python
from nextpy.components.radix.primitives.progress import progress_indicator

# Create a progress indicator that fills half the progress bar
progress_bar_indicator = progress_indicator(value=50)
```

### Components

#### Properties

| Prop Name    | Type                           | Description                                     |
|--------------|--------------------------------|-------------------------------------------------|
| `value`      | `Optional[Union[Var[int], int]]` | The current value of the progress indicator.    |
| `style`      | `Optional[Style]`              | The style applied to the progress indicator.    |
| `class_name` | `Optional[Any]`                | The class name for custom CSS styling.          |

#### Event Triggers

Event triggers are similar to those in `ProgressRoot`.

### Best Practices

- Use `ProgressIndicator` inside a `ProgressRoot` to represent the filled portion of the progress bar.
- The `value` prop should be less than or equal to the `max` value of the enclosing `ProgressRoot`.

## Notes

- The `ProgressRoot` and `ProgressIndicator` components should be used together to represent progress bars effectively.
- Keep accessibility in mind by providing textual representations of progress where necessary.
- Avoid using too many progress bars on the same view to prevent clutter and confusion.

This documentation serves as a guide for developers to effectively implement and utilize the Progress components in their Nextpy-based web applications.