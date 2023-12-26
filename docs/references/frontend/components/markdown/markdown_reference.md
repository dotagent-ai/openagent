##  Reference for nextpy/frontend/components/markdown/markdown.pyi

# Nextpy Markdown Component Documentation

## Markdown

The Markdown component in Nextpy allows you to render Markdown text within your Python application. It's particularly useful for displaying rich text, code snippets, or any content that follows Markdown syntax, including support for LaTeX math expressions and GitHub Flavored Markdown (GFM).

### Anatomy

The `Markdown` component can be instantiated with various parameters to customize its behavior and appearance. Below you'll find basic and advanced usage examples.

#### Basic Usage

```python
from nextpy.components.markdown import Markdown

markdown_text = """
# Heading

This is a paragraph with *emphasis* and **strong importance**.

- List item 1
- List item 2
- List item 3

`Code snippet`
"""

markdown_component = Markdown.create(markdown_text)
```

#### Advanced Usage

```python
from nextpy.components.markdown import Markdown
from nextpy.frontend.style import Style

custom_styles = {
    "p": lambda props: Text.create(**props, style=Style(color="blue")),
    "li": lambda props: ListItem.create(**props, style=Style(color="green"))
}

custom_component_map = {
    "Text": Text,
    "ListItem": ListItem,
}

markdown_text = """
# Custom Styled Heading

This is a blue paragraph.

- Green list item
"""

markdown_component = Markdown.create(
    markdown_text,
    component_map=custom_component_map,
    custom_styles=custom_styles,
    style=Style(background_color="lightgray")
)
```

### Components

The Markdown component uses a variety of sub-components to render different Markdown elements, such as text paragraphs, lists, and links. You can customize these sub-components using a component map.

- **Text**: Renders normal text.
- **Heading**: Renders headings from `#` to `######`.
- **ListItem**, **OrderedList**, **UnorderedList**: Render list items and lists.
- **Link**: Renders hyperlinks.

| Prop Name          | Type                                                  | Description                                      |
|--------------------|-------------------------------------------------------|--------------------------------------------------|
| component_map      | Dict[str, Any]                                        | Map of tag to component creation function.       |
| custom_styles      | Dict[str, Any]                                        | Custom styles for the markdown (deprecated).     |
| component_map_hash | str                                                   | Hash of the component map.                       |
| style              | Style                                                 | Style of the component.                          |
| key                | Any                                                   | A unique key for the component.                  |
| id                 | Any                                                   | The id for the component.                        |
| class_name         | Any                                                   | The class name for the component.                |
| autofocus          | bool                                                  | Autofocus the component on page load.            |
| custom_attrs       | Dict[str, Union[Var, str]]                            | Custom attributes for the component.             |
| on_blur            | Union[EventHandler, EventSpec, list, function, BaseVar] | Event handler for blur events.                |
| on_click           | ... (similar for other events)                        | Event handlers for various mouse and UI events.  |

### Notes

- The `component_map` allows you to define custom rendering for Markdown tags. This is useful for integrating your own components or styling into the Markdown rendering.
- The `custom_styles` prop is deprecated as of version 0.2.9; use the `component_map` for customization instead.
- Avoid using the `key` prop unless you are rendering multiple Markdown components in a list.
- Event handlers such as `on_click` can be attached to the Markdown component to handle various events.

### Best Practices

- Keep the Markdown content clean and structured for better readability and easier maintenance.
- Use the `component_map` for custom styling and overriding default components.
- If performance is a concern, consider memoizing components that are frequently re-rendered with the same properties.
- Use Markdown for displaying user-generated content, documentation, or any text-based content that benefits from rich formatting.
- Remember to sanitize any user-generated Markdown to prevent XSS attacks if you're rendering Markdown from user input.

This documentation provides a comprehensive overview of the Markdown component in Nextpy, designed to assist developers in effectively utilizing the component in their full-stack Python applications.