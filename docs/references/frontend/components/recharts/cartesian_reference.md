##  Reference for nextpy/frontend/components/recharts/cartesian.pyi

# Nextpy Documentation: Recharts Components

This documentation covers the set of components provided by Nextpy for creating charts using Recharts, a popular charting library built on top of ReactJS.

## Axis

The `Axis` component is a fundamental part of a chart that helps understand the data better by providing scale and context.

### Anatomy

```python
from nextpy.components.recharts import Axis

axis = Axis.create(
    data_key="frequency",
    hide=False,
    orientation="bottom",
    type_="number",
    allow_decimals=True,
    allow_data_overflow=False,
    scale="linear"
)
```

### Components

#### Properties

| Prop Name               | Type                  | Description                                              |
|-------------------------|-----------------------|----------------------------------------------------------|
| `data_key`              | `str` or `int`        | Unique identifier for a group of data within a chart.    |
| `hide`                  | `bool`                | Toggle the visibility of the axis.                       |
| `orientation`           | `str`                 | The orientation of the axis: "top" or "bottom".          |
| `type_`                 | `str`                 | Type of axis: "number" or "category".                    |
| `allow_decimals`        | `bool`                | Allows displaying decimal values on the axis.            |
| `allow_data_overflow`   | `bool`                | Determines if data should be clipped to the axis domain. |
| `scale`                 | `str`                 | Type of scale function to use for the axis.              |

#### Event Triggers

- `on_click`
- `on_mouse_enter`
- `on_mouse_leave`
- `on_mouse_move`
- `on_mouse_out`
- `on_mouse_over`

### Notes

- When using `allow_data_overflow`, ensure that your data is appropriately scaled to avoid unexpected visual issues.
- The `orientation` should be set according to the chart layout.

### Best Practices

- Use clear and concise labels for axes to improve readability.
- Select a scale that best represents your data and makes the chart easy to interpret.

---

## XAxis and YAxis

`XAxis` and `YAxis` components specifically control the horizontal and vertical axes of a chart, respectively. They inherit properties from `Axis`.

### Anatomy

```python
from nextpy.components.recharts import XAxis, YAxis

x_axis = XAxis.create(
    data_key="name",
    hide=False,
    orientation="bottom",
    type_="category"
)

y_axis = YAxis.create(
    data_key="value",
    hide=False,
    orientation="left",
    type_="number",
    scale="linear"
)
```

---

## ZAxis

The `ZAxis` component is used for defining a third axis in a 3D data set or a scatter plot.

### Anatomy

```python
from nextpy.components.recharts import ZAxis

z_axis = ZAxis.create(
    data_key="volume",
    range=[100, 1000],
    scale="linear"
)
```

---

## Brush

The `Brush` component is used for selecting a subset of data to display on the chart.

### Anatomy

```python
from nextpy.components.recharts import Brush

brush = Brush.create(
    stroke="#8884d8",
    data_key="time",
    traveller_width=10
)
```

### Notes

- The `Brush` component is often used in conjunction with a larger data set to provide a zoomed-in view.

---

## Cartesian

The `Cartesian` component is the base for plotting Cartesian components on the chart, such as `Area`, `Bar`, `Line`, and `Scatter`.

### Anatomy

```python
from nextpy.components.recharts import Cartesian, Area

cartesian = Cartesian.create(
    layout="horizontal"
)

area_chart = Area.create(
    stroke="#8884d8",
    fill="#8884d8",
    data_key="value"
)
```

### Notes

- The `layout` property determines the orientation of the plotted data.

### Best Practices

- Combine different Cartesian components to create composite charts for complex data analysis.

---

## Area

The `Area` component is used for representing quantities through filled areas on the chart.

### Anatomy

```python
from nextpy.components.recharts import Area

area = Area.create(
    stroke="#8884d8",
    fill="#8884d8",
    data_key="value",
    type_="monotone"
)
```

### Notes

- The `type_` property controls the shape of the area curve.

---

## Bar

The `Bar` component is used for creating bar charts.

### Anatomy

```python
from nextpy.components.recharts import Bar

bar = Bar.create(
    fill="#8884d8",
    data_key="value",
    bar_size=20
)
```

---

## Line

The `Line` component is used for drawing lines on a chart, typically for line charts.

### Anatomy

```python
from nextpy.components.recharts import Line

line = Line.create(
    stroke="#8884d8",
    data_key="value",
    type_="monotone"
)
```

---

## Scatter

The `Scatter` component is used for creating scatter plots.

### Anatomy

```python
from nextpy.components.recharts import Scatter

scatter = Scatter.create(
    data=[...],
    fill="#8884d8",
    shape="star"
)
```

---

## Funnel

The `Funnel` component is used for creating funnel charts, which are effective for representing stages in a process.

### Anatomy

```python
from nextpy.components.recharts import Funnel

funnel = Funnel.create(
    data=[...],
    animation_duration=1500
)
```

---

## ErrorBar

The `ErrorBar` component is used to represent the variability of the data on other chart components like `Bar` or `Line`.

### Anatomy

```python
from nextpy.components.recharts import ErrorBar

error_bar = ErrorBar.create(
    data_key="error",
    direction="y",
    stroke="#8884d8"
)
```

---

## Reference

The `Reference` components (`ReferenceLine`, `ReferenceDot`, `ReferenceArea`) are used for drawing extra elements like lines, dots, and areas to highlight certain parts of the chart.

### Anatomy

```python
from nextpy.components.recharts import ReferenceLine

reference_line = ReferenceLine.create(
    stroke="red",
    if_overflow="extendDomain",
    y=400
)
```

---

## Grid

The `Grid` component, specifically `CartesianGrid`, is used for drawing a grid within the chart area.

### Anatomy

```python
from nextpy.components.recharts import CartesianGrid

grid = CartesianGrid.create(
    stroke_dasharray="3 3"
)
```

### Notes

- Customize the `stroke_dasharray` for different grid line styles.

---

## CartesianAxis

The `CartesianAxis` component represents the axes in a Cartesian grid.

### Anatomy

```python
from nextpy.components.recharts import CartesianAxis

axis = CartesianAxis.create(
    orientation="bottom",
    tick_line=False
)
```

### Notes

- The `orientation` property determines the position and orientation of the axis.

---

The Nextpy Recharts components provide a flexible and powerful way to visualize data. The documentation above should serve as a guide to effectively use these components to create insightful and interactive charts for your data.