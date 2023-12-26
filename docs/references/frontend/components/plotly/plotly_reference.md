##  Reference for nextpy/frontend/components/plotly/plotly.pyi

# Plotly

## Overview

The `Plotly` component in Nextpy allows for the integration of interactive and rich graphical plots into the Nextpy web applications. Leveraging the capabilities of the Plotly library, it enables developers to create a wide variety of charts and visualizations that are both appealing and informative.

## Purpose

The primary purpose of the `Plotly` component is to provide an easy-to-use interface for rendering Plotly figures and graphs within a Nextpy application. It is designed to work seamlessly with the Plotly Python library, which is well-known for its comprehensive set of chart types, ranging from basic line and bar charts to complex 3D models and geographical maps.

## Use Cases

The `Plotly` component is useful in scenarios where data visualization is crucial, such as:

- Data analysis and reporting dashboards.
- Financial, economic, and scientific research.
- Real-time data monitoring systems.
- Educational tools to illustrate complex concepts visually.

## Structure and Usage

To use the `Plotly` component, you need to import it and then use its `create` method to instantiate it with the required data and layout configurations.

```python
from nextpy.components.plotly import Plotly

# Assuming 'fig' is a Plotly Figure object
plotly_component = Plotly.create(data=fig)
```

## Anatomy

### Basic Implementation

Here's a simple example to create a line chart using the `Plotly` component:

```python
from nextpy.components.plotly import Plotly
import plotly.graph_objs as go

# Create a simple line plot
line_fig = go.Figure(data=go.Scatter(x=[1, 2, 3], y=[4, 1, 2]))

# Use the Plotly component to render the figure
line_chart = Plotly.create(data=line_fig)
```

### Advanced Implementation

For a more complex graph with additional styling and layout options:

```python
from nextpy.components.plotly import Plotly
import plotly.graph_objs as go

# Create a complex plot with layout and style configurations
complex_fig = go.Figure(
    data=[
        go.Bar(x=[1, 2, 3], y=[4, 1, 2], name='Bar'),
        go.Line(x=[1, 2, 3], y=[2, 3, 4], name='Line')
    ],
    layout=go.Layout(title='Complex Plot', showlegend=True)
)

# Use the Plotly component to render the complex figure
complex_chart = Plotly.create(
    data=complex_fig,
    layout={'title': 'My Complex Chart'},
    style={'width': '100%', 'height': '400px'}
)
```

## Components

### Properties

| Prop Name           | Type                                         | Description                                                    |
|---------------------|----------------------------------------------|----------------------------------------------------------------|
| data                | `Union[Var[Figure], Figure]`                 | The figure object from Plotly to be displayed.                 |
| layout              | `Union[Var[Dict], Dict]`                     | Optional layout configuration for the plot.                    |
| width               | `Union[Var[str], str]`                       | Optional width of the plot, can be in pixels or percentage.    |
| height              | `Union[Var[str], str]`                       | Optional height of the plot, can be in pixels or percentage.   |
| use_resize_handler  | `Union[Var[bool], bool]`                     | If `True`, the plot will resize on window resize events.       |
| style               | `Style`                                      | CSS style properties for the component.                        |
| key                 | `Any`                                        | A unique key for the component.                                |
| id                  | `Any`                                        | The DOM id for the component.                                  |
| class_name          | `Any`                                        | The CSS class name for the component.                          |
| autofocus           | `bool`                                       | If `True`, the component will be focused on page load.         |
| custom_attrs        | `Dict[str, Union[Var, str]]`                 | Custom attributes to pass to the underlying HTML element.      |
| on_* (event handlers) | `Union[EventHandler, EventSpec, list, function, BaseVar]` | Event handlers for corresponding DOM events. |

## Notes

- Make sure you have the Plotly library installed in your environment to use this component.
- The component does not support server-side rendering (NoSSRComponent).

## Best Practices

- To ensure responsiveness, consider setting the width and height properties as percentages.
- Utilize the `use_resize_handler` property for dynamic resizing in responsive layouts.
- When dealing with large datasets or complex plots, be mindful of performance. Optimize your Plotly figures to ensure a smooth user experience.
- Use appropriate layout and styling to make the plot accessible and easy to understand for the end-users.
- Always test the interactivity of your plots across different devices and browsers.