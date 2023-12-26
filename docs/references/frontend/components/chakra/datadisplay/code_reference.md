##  Reference for nextpy/frontend/components/chakra/datadisplay/code.pyi

# Nextpy Documentation

## `CodeBlock` Component

### Overview

The `CodeBlock` component is designed to display blocks of code in a styled and formatted manner within a Nextpy application. It is especially useful for tutorials, documentation, or any scenario where presenting source code is necessary. The component supports syntax highlighting and offers various theming options to match the style of your application.

### Use Cases

- Displaying example code snippets in tutorials.
- Showing configuration examples in documentation.
- Exhibiting sample code in blogs or articles related to programming.
- Embedding source code in educational content for coding lessons.

### Structure and Usage

`CodeBlock` wraps a block of code with syntax highlighting and optional line numbers. It can be themed and customized to fit the look and feel of your application.

### Anatomy

#### Basic Implementation

```python
from nextpy.components.chakra.datadisplay import CodeBlock

code_snippet = """
def hello_world():
    print("Hello, World!")
"""

code_block = CodeBlock.create(
    code=code_snippet,
    language="python",
    theme="dracula",
    show_line_numbers=True
)
```

#### Advanced Implementation

```python
from nextpy.components.chakra.datadisplay import CodeBlock
from nextpy.backend.vars import Var

# Using a dynamic variable for code and theming
code_var = Var("""
def greet(name):
    print(f"Hello, {name}!")
""")

theme_var = Var("one-dark")

code_block = CodeBlock.create(
    code=code_var,
    language="python",
    theme=theme_var,
    show_line_numbers=True,
    can_copy=True,
    wrap_long_lines=True,
    starting_line_number=10
)
```

### Components

- `can_copy`: Whether a copy button should appear to allow users to copy the code snippet.
- `copy_button`: A custom copy button component to override the default one.
- `theme`: The visual theme for the code block (e.g., "light", "dark", "dracula").
- `language`: The programming language of the code block for proper syntax highlighting.
- `code`: The code content to be displayed in the `CodeBlock`.
- `show_line_numbers`: Whether to display line numbers next to the code block.
- `starting_line_number`: The starting line number to use if line numbers are enabled.
- `wrap_long_lines`: Whether to wrap long lines that exceed the width of the container.
- `custom_style`: A custom style dictionary to apply additional CSS to the code block.
- `code_tag_props`: Additional properties passed down to the `<code>` HTML tag.

### Notes

- Ensure that the `language` prop is set to a valid option for proper syntax highlighting.
- When using custom theming, validate that the theme works well with the overall design of your application.
- If enabling the copy feature, consider the placement of the copy button for the best user experience.

### Best Practices

- Keep the code snippets concise and focused on the topic being discussed or demonstrated.
- Use themes that provide sufficient contrast between the text and background for readability.
- When providing code examples, include comments within the code to explain complex or important parts.
- Customize the starting line number when displaying an excerpt from a larger codebase to maintain context.