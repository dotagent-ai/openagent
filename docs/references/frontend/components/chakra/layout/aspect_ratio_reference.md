##  Reference for nextpy/frontend/components/chakra/layout/aspect_ratio.pyi

# Nextpy Documentation

## AspectRatio Component

The `AspectRatio` component in Nextpy is designed to ensure that a child component maintains a specific aspect ratio. This is particularly useful for embedding content like videos or slideshows, where maintaining the correct width-to-height ratio is important for proper display.

### Anatomy

To implement the `AspectRatio` component, you'll first import it from the Nextpy library and then use the `create` method to instantiate it. Here's a basic example that maintains a 16:9 aspect ratio:

```python
from nextpy.components.chakra.layout.aspect_ratio import AspectRatio

aspect_ratio_box = AspectRatio.create(
    # child components here,
    ratio=16/9
)
```

In this example, any children placed within `aspect_ratio_box` will scale properly while maintaining the 16:9 aspect ratio.

For more advanced use cases, you can customize the `AspectRatio` component with additional parameters, like `style`, `id`, `class_name`, etc. Here's how you might use some of these advanced options:

```python
aspect_ratio_box = AspectRatio.create(
    # child components here,
    ratio=16/9,
    style=Style(padding="20px", background_color="#f0f0f0"),
    id="video-aspect-ratio",
    class_name="responsive-video",
    on_click=lambda event: print("Video clicked")
)
```

### Components

The `AspectRatio` component consists of the following properties and event handlers:

#### Properties

| Prop Name     | Type                                            | Description                                                  |
|---------------|-------------------------------------------------|--------------------------------------------------------------|
| ratio         | Optional[Union[Var[float], float]]              | The aspect ratio to maintain.                                |
| style         | Optional[Style]                                 | Styling options for the component.                           |
| key           | Optional[Any]                                   | A unique key for the component.                              |
| id            | Optional[Any]                                   | The id for the component.                                    |
| class_name    | Optional[Any]                                   | The class name for the component.                            |
| autofocus     | Optional[bool]                                  | Autofocuses the component when the page loads.               |
| custom_attrs  | Optional[Dict[str, Union[Var, str]]]            | Custom attributes for the component.                         |

#### Event Handlers

| Event Name        | Type                                                        | Description                                          |
|-------------------|-------------------------------------------------------------|------------------------------------------------------|
| on_blur           | Optional[Union[EventHandler, EventSpec, list, function]]    | Event triggered when the component loses focus.      |
| on_click          | Optional[Union[EventHandler, EventSpec, list, function]]    | Event triggered when the component is clicked.       |
| on_context_menu   | Optional[Union[EventHandler, EventSpec, list, function]]    | Event triggered on a right-click.                    |
| ...               | ...                                                         | ...                                                  |

Note: The `...` indicates that all standard event handlers applicable to HTML elements are available and can be used similarly.

### Notes

- The `ratio` property is critical and must be provided to ensure the component functions as intended.
- Children of the `AspectRatio` component will automatically scale to maintain the specified aspect ratio.

### Best Practices

- Use `AspectRatio` for media elements that need to maintain a specific size ratio to prevent layout issues on different screen sizes.
- Combine with responsive design techniques to ensure a seamless user experience across devices.
- Avoid nesting `AspectRatio` components within each other, as this can lead to unexpected behaviors.

By following these practices and using the properties and event handlers effectively, you can create a visually stable and responsive UI with the `AspectRatio` component in Nextpy.