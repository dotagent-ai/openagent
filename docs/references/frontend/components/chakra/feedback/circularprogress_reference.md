##  Reference for nextpy/frontend/components/chakra/feedback/circularprogress.pyi

# Nextpy Documentation: CircularProgress Component

## CircularProgress

### Overview

The `CircularProgress` component is a visual indicator used to show the progress of an ongoing task or operation. It can be used to provide feedback to users about the loading state of an application, the completion of a file upload, or any other process that requires a representation of progression.

### Purpose

The purpose of `CircularProgress` is to offer a clear and immediate visual cue to users that an operation is in progress, how much of it has been completed, and whether it is indeterminate (i.e., the duration or completion percentage is unknown).

### Use Cases

- Displaying the progress of a file download or upload.
- Indicating that a page or component is loading.
- Showing the status of a background task, such as data processing.
- Providing feedback during a form submission.

### Structure and Usage

`CircularProgress` consists of a circular track with a fill that represents the progress. It can be determinate (showing an actual percentage of completion) or indeterminate (showing an ongoing process without a defined endpoint).

#### Anatomy

**Basic Implementation:**

```python
circular_progress = CircularProgress.create(
    value=Var(50),
    max_=Var(100),
    min_=Var(0),
    thickness=Var("4px"),
    track_color="gray.200",
    color="blue.500",
)
```

**Advanced Implementation:**

```python
circular_progress_with_label = CircularProgress.create(
    value=Var(75),
    max_=Var(100),
    min_=Var(0),
    is_indeterminate=Var(False),
    color="green.400",
    size="120px"
)
circular_progress_label = CircularProgressLabel.create(
    "75%"
)
circular_progress.add_child(circular_progress_label)
```

### Components

**`CircularProgress` Properties:**

| Prop Name         | Type                            | Description                                                |
|-------------------|---------------------------------|------------------------------------------------------------|
| label             | `str`, `Var[str]`               | Text label to display inside the circular progress.        |
| cap_is_round      | `bool`, `Var[bool]`             | Whether the progress indicator cap is rounded.             |
| is_indeterminate  | `bool`, `Var[bool]`             | Whether the progress is indeterminate.                     |
| max_              | `int`, `Var[int]`               | Maximum value for the progress.                            |
| min_              | `int`, `Var[int]`               | Minimum value for the progress.                            |
| thickness         | `str`, `int`, `Var[...]`        | Stroke width of the svg circle.                            |
| track_color       | `str`, `Var[str]`               | Color of the progress track.                               |
| value             | `int`, `Var[int]`               | Current progress value.                                    |
| value_text        | `str`, `Var[str]`               | Custom text to display instead of the progress value.      |
| color             | `str`, `Var[str]`               | Color of the progress bar.                                 |
| size              | `str`, `Var[str]`               | Size of the circular progress.                             |
| style             | `Style`                         | Style object for custom styles.                            |
| ...               |                                 | Additional properties inherited from `ChakraComponent`.    |

### Notes

- The `value` property must be between `min_` and `max_`.
- When `is_indeterminate` is set to `True`, the `value` property is ignored.
- Ensure proper contrast between the `track_color` and `color` for better visibility.

### Best Practices

- Use `CircularProgress` to indicate loading or progress only when necessary to avoid distracting users.
- If using a label, ensure it is concise and provides meaningful information about the progress.
- Customize the size and color to fit the application's design, but maintain readability and accessibility.
- For indeterminate progress, use animations to give users a sense that something is happening, even if the duration is unknown.

Remember to always test the component's appearance and functionality across different browsers and devices to ensure consistent user experience.