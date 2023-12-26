##  Reference for nextpy/frontend/components/chakra/disclosure/transition.pyi

# Nextpy Documentation: Transition Components

## Transition

### Overview

The `Transition` component in Nextpy is designed to provide animation effects when a component enters or exits the DOM. This component serves as the base for various specialized transition components such as `Fade`, `ScaleFade`, `Slide`, `SlideFade`, and `Collapse`. It allows developers to create more dynamic, responsive, and visually appealing interfaces.

### Anatomy

Here's a basic example of how you can use the `Transition` component:

```python
from nextpy.components.chakra.disclosure.transition import Transition

# Using the Transition component to animate the appearance of a div
transition_component = Transition.create(
    in_=True,
    unmount_on_exit=True,
    children=[
        Div.create("Content to reveal")
    ]
)
```

### Components

- `Fade`: Applies a fade transition to its children.
- `ScaleFade`: Applies a scaling and fading transition.
- `Slide`: Slides its children from a specified direction.
- `SlideFade`: Combines sliding and fading effects.
- `Collapse`: Animates the expansion or collapse of its children.

### Properties Table

Common properties for the transition components:

| Prop Name       | Type                     | Description                                                               |
|-----------------|--------------------------|---------------------------------------------------------------------------|
| `in_`           | `Union[Var[bool], bool]` | If `True`, the component will transition in; if `False`, it will transition out. |
| `unmount_on_exit` | `Union[Var[bool], bool]` | If `True`, the component unmounts after the exit transition completes.  |
| `style`         | `Style`                  | The CSS styles to apply to the component.                                 |
| `key`           | `Any`                    | A unique key for the component (useful in lists).                         |
| `id`            | `Any`                    | The id attribute of the component.                                        |
| `class_name`    | `Any`                    | The class attribute of the component.                                     |
| `autofocus`     | `bool`                   | If `True`, the component will be focused automatically when the page loads. |
| `custom_attrs`  | `Dict[str, Union[Var, str]]` | Custom attributes to pass to the component.                            |

> Note: Additional properties are specific to each transition type, such as `direction` for `Slide`, `initial_scale` for `ScaleFade`, and `offsetX`/`offsetY` for `SlideFade`.

### Notes

- The transition components utilize CSS transitions, so ensure your project includes the necessary CSS for these animations.
- When using `unmount_on_exit`, remember that the component's state will be lost when it's removed from the DOM.

### Best Practices

- Utilize transition components to improve user experience by providing visual cues for dynamic content changes.
- Keep animations performant by not overusing them and ensuring they run smoothly on all target devices.
- Test the accessibility of your application, as transitions can sometimes affect users with visual impairments.

### Advanced Example

Combining multiple transition components for a complex animation:

```python
from nextpy.components.chakra.disclosure.transition import Fade, Slide, ScaleFade

# Combining Fade and Slide transitions for a notification component
notification = Slide.create(
    direction="top",
    in_=True,
    children=[
        Fade.create(
            in_=True,
            children=[
                ScaleFade.create(
                    initial_scale=0.9,
                    in_=True,
                    children=[
                        Div.create("Your action was successful!")
                    ]
                )
            ]
        )
    ]
)
```

Here, a notification message first slides in from the top, then fades in, and finally scales up slightly for emphasis.