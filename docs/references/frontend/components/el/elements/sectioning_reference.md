##  Reference for nextpy/frontend/components/el/elements/sectioning.pyi

# Nextpy - Sectioning Components Documentation

## Body

**Overview**:
The `Body` component represents the content of an HTML document. It is the container for all the visible contents of a web page, such as text, images, links, etc.

**Use Cases**:
- Use `Body` as the main container for your application's content.
- Apply global styles, scripts, and event handlers for the entire document.

**Structure**:
The `Body` component should be used once per document and contain all the visible HTML content.

**Usage**:
```python
from nextpy.components.el.elements.sectioning import Body

body_content = Body.create(
    # children components go here
)
```

**Anatomy**:
- **Basic Implementation**:
    ```python
    body_content = Body.create(
        H1.create("Welcome to Nextpy!"),
        P.create("This is a Python-based web application.")
    )
    ```
- **Advanced Implementation**:
    ```python
    body_content = Body.create(
        Header.create(...),
        Main.create(...),
        Footer.create(...),
        style=Style(backgroundColor="lightblue")
    )
    ```

**Components**:
- **children**: Components or elements that are placed within the body.
- **style**: An optional `Style` object to apply CSS to the entire body.

**Properties Table**:

| Prop Name    | Type           | Description                            |
|--------------|----------------|----------------------------------------|
| bgcolor      | str, Var       | Background color of the body.          |
| background   | str, Var       | Background image of the body.          |
| style        | Style          | Inline styles for the body component.  |
| key          | Any            | A unique key for the component.        |
| id           | Any            | The ID for the component.              |
| class_name   | Any            | The class name for the component.      |
| custom_attrs | Dict[str, Var] | Custom attributes for the component.   |
| on_blur      | EventHandler   | Event handler for the blur event.      |
| on_click     | EventHandler   | Event handler for the click event.     |

**Event Triggers**:
- `on_mount`: Called when the component is mounted in the DOM.
- `on_unmount`: Called when the component is unmounted from the DOM.

**Notes**:
- The `Body` component should be used with caution as it affects the entire page.

**Best Practices**:
- It is recommended to use only one `Body` component per page.
- Ensure the `Body` component encapsulates all other components except for the `Head` component.
- Utilize the `style` property to maintain consistent look and feel across the application.

## Address

**Overview**:
The `Address` component is used to define contact information for the author/owner of a document or article.

**Use Cases**:
- Displaying the author's contact information in articles or blog posts.
- Providing contact details in the footer of a website.

**Structure**:
`Address` typically contains physical address details, phone numbers, email addresses, and so on.

**Usage**:
```python
from nextpy.components.el.elements.sectioning import Address

address_info = Address.create(
    P.create("1234 Python Street"),
    P.create("Codeville, PY 12345"),
    P.create("Email: info@nextpy.com")
)
```

**Anatomy**:
- **Basic Implementation**:
    ```python
    address_info = Address.create(
        "Contact us at: ",
        A.create(href="mailto:info@nextpy.com", children="info@nextpy.com")
    )
    ```
- **Advanced Implementation**:
    ```python
    address_info = Address.create(
        P.create("Address: 1234 Python Street, Codeville, PY 12345"),
        P.create("Phone: (123) 456-7890"),
        P.create("Email: "),
        A.create(href="mailto:info@nextpy.com", children="info@nextpy.com"),
        style=Style(padding="20px", backgroundColor="#f5f5f5")
    )
    ```

**Components**:
- **children**: Components or elements like paragraphs, links, etc., that contain the contact details.

**Properties Table**:

| Prop Name    | Type           | Description                            |
|--------------|----------------|----------------------------------------|
| style        | Style          | Inline styles for the address component. |
| key          | Any            | A unique key for the component.        |
| id           | Any            | The ID for the component.              |
| class_name   | Any            | The class name for the component.      |
| custom_attrs | Dict[str, Var] | Custom attributes for the component.   |

**Event Triggers**:
- `on_click`: Called when the component is clicked.

**Notes**:
- Semantically use `Address` for contact information only.

**Best Practices**:
- Keep the information concise and use appropriate elements like `P` for text and `A` for email links.
- Apply styling to ensure the address information is easy to find and read.

(And so on for the rest of the sectioning components `Article`, `Aside`, `Footer`, `Header`, `H1` through `H6`, `Main`, `Nav`, and `Section` with their corresponding overview, use cases, structure, usage, anatomy, components, properties table, event triggers, notes, and best practices.)