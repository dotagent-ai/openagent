##  Reference for nextpy/frontend/components/chakra/forms/slider.pyi

# Nextpy Documentation - Slider Component

## Slider

### Overview

The `Slider` component in Nextpy is a user interface element that allows users to select a value from a range by sliding a thumb along a track. It's commonly used in forms for adjusting settings, such as volume control or selecting a numeric value within a defined range.

### Use Cases

- Adjusting a numerical parameter within an application, such as font size or brightness.
- Filtering data based on a range selection, like price filters on e-commerce sites.
- Controlling media playback volume or seek position in multimedia applications.

### Structure

The `Slider` component consists of several parts:

- **SliderTrack**: The visual representation of the range available for selection.
- **SliderFilledTrack**: The portion of the track which shows the selected value.
- **SliderThumb**: The draggable circle that represents the value currently chosen.
- **SliderMark**: Optional marks along the track that indicate specific values.

### Usage

Basic implementation:

```python
import nextpy as npy

slider_value = npy.Var(50)

slider = npy.Slider.create(
    value=slider_value,
    min_=0,
    max_=100,
    step=1
)

# To display the slider in the app
npy.render(slider)
```

Advanced implementation with custom styles and event handling:

```python
import nextpy as npy

slider_value = npy.Var(30)

def on_slider_change(event):
    print(f"Slider value changed to {event.value}")

slider = npy.Slider.create(
    value=slider_value,
    min_=0,
    max_=100,
    step=5,
    color_scheme='blue',
    on_change=on_slider_change,
    style=npy.Style(margin='10px')
)

# To display the slider in the app
npy.render(slider)
```

### Components

#### Slider

| Prop Name                | Type                    | Description                                                        |
|--------------------------|-------------------------|--------------------------------------------------------------------|
| value                    | `Var[int], int`         | The current value of the slider.                                   |
| color_scheme             | `Var[str], str`         | The color scheme of the slider track and thumb.                    |
| default_value            | `Var[int], int`         | The initial value when the slider is first rendered.               |
| direction                | `Var[str], str`         | The text direction, either "ltr" (left-to-right) or "rtl" (right-to-left). |
| focus_thumb_on_change    | `Var[bool], bool`       | If true, focuses the thumb when the value changes.                 |
| is_disabled              | `Var[bool], bool`       | If true, disables the slider.                                      |
| is_read_only             | `Var[bool], bool`       | If true, the slider will be read-only.                             |
| is_reversed              | `Var[bool], bool`       | If true, the slider will be reversed.                              |
| min_                     | `Var[int], int`         | The minimum value of the slider.                                   |
| max_                     | `Var[int], int`         | The maximum value of the slider.                                   |
| step                     | `Var[int], int`         | The step increment of the slider.                                  |
| min_steps_between_thumbs | `Var[int], int`         | The minimum steps between thumbs for range sliders.                |
| orientation              | `Var[str], str`         | The orientation of the slider, either "horizontal" or "vertical".  |
| name                     | `Var[str], str`         | The form field name for the slider.                                |
| style                    | `Style`                 | The style object for custom styling.                               |
| on_change                | `EventHandler, EventSpec` | Callback for when the slider value changes.                       |
| on_change_end            | `EventHandler, EventSpec` | Callback for when the change of slider value is finished.         |
| on_change_start          | `EventHandler, EventSpec` | Callback for when the change of slider value begins.              |

### Notes

- Ensure the `value` prop is a `Var` if you want to make it stateful and responsive to changes.
- Use appropriate `min_` and `max_` values to define the slider's range, and set a reasonable `step` value.
- Always provide an `on_change` handler to perform actions based on the slider's value.

### Best Practices

- Use clear labels to indicate what the slider controls.
- Implement feedback mechanisms, like a tooltip or a value display, to provide immediate feedback on the slider's position.
- Avoid using very small step values which might make the slider hard to control for the user.
- Group sliders logically and provide adequate spacing between them for better user interaction.
- Consider accessibility by ensuring the slider is operable through keyboard inputs and screen readers.

Following these guidelines will help you create effective, user-friendly sliders that enhance the user experience of your application.