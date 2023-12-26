##  Reference for nextpy/frontend/components/el/elements/metadata.pyi

# Nextpy Documentation: Metadata Components

This section of the documentation covers the metadata components available in the Nextpy library, which are used to define the metadata of an HTML document. Metadata is data about data and in the case of an HTML document, it typically defines details such as the character set, page description, keywords, author of the document, and more.

## Base

The `Base` component represents the HTML `<base>` element, which specifies the base URL to use for all relative URLs in a document.

### Anatomy

```python
# Basic usage of the Base component
base_component = Base.create(
    href="https://www.example.com/",
    target="_blank"
)
```

### Components

| Prop Name          | Type        | Description                                                                                          |
|--------------------|-------------|------------------------------------------------------------------------------------------------------|
| href               | `str`       | The base URL to be used throughout the document for relative URLs.                                   |
| target             | `str`       | Specifies the default target for all hyperlinks and forms in the document.                           |

### Notes

- The `Base` component must appear within the `<head>` of the document and only one `<base>` element is allowed in a document.

### Best Practices

- Define the `Base` component early in the document head to ensure it affects all relative URLs.

## Head

The `Head` component is a container for all the head elements, which can include `Title`, `Meta`, and `Link` components, among others.

### Anatomy

```python
# Basic usage of the Head component
head_component = Head.create(
    Title.create("Page Title"),
    Meta.create(name="description", content="A description of the page"),
    Link.create(rel="stylesheet", href="/styles.css")
)
```

### Notes

- The `Head` component is not to be confused with the HTML `<head>` element; it acts as a container for elements that would typically be found in the head of an HTML document.

## Link

The `Link` component represents the HTML `<link>` element used to link to external resources like CSS files.

### Anatomy

```python
# Basic usage of the Link component
link_component = Link.create(
    rel="stylesheet",
    href="/styles.css"
)
```

### Components

| Prop Name         | Type        | Description                                                                    |
|-------------------|-------------|--------------------------------------------------------------------------------|
| cross_origin      | `str`       | How the element handles cross-origin requests.                                 |
| href              | `str`       | The URL of the linked resource.                                                |
| href_lang         | `str`       | The language of the text in the linked resource.                               |
| integrity         | `str`       | Security feature that allows browsers to verify what they fetch.                |
| media             | `str`       | Specifies what media/device the linked document is optimized for.               |
| referrer_policy   | `str`       | Specifies which referrer information to send with the request for the resource. |
| rel               | `str`       | Specifies the relationship between the current document and the linked document.|
| sizes             | `str`       | Sizes of icons (for rel="icon").                                               |
| type              | `str`       | Specifies the media type of the linked resource.                               |

### Best Practices

- Use the `Link` component to include stylesheets, preconnect to required origins, and load icons.

## Meta

The `Meta` component represents the HTML `<meta>` element used to specify metadata that cannot be represented by other HTML meta-related elements like `Base`, `Link`, and `Title`.

### Anatomy

```python
# Basic usage of the Meta component
meta_component = Meta.create(
    char_set="UTF-8",
    name="viewport",
    content="width=device-width, initial-scale=1.0"
)
```

### Components

| Prop Name         | Type        | Description                                                                   |
|-------------------|-------------|-------------------------------------------------------------------------------|
| char_set          | `str`       | Specifies the character encoding for the HTML document.                       |
| content           | `str`       | Gives the value associated with the `http-equiv` or `name` attribute.         |
| http_equiv        | `str`       | Provides HTTP headers for the information/value of the content attribute.     |
| name              | `str`       | Specifies a name for the metadata.                                            |

### Notes

- `Meta` components are typically placed in the document head and are used by browsers (how to display content or reload page), search engines (keywords), and other web services.

### Best Practices

- Use `Meta` components to define settings such as viewport, character set, and description for search engine optimization.

## Title

The `Title` component represents the HTML `<title>` element, which defines the title of the document, shown in a browser's title bar or page's tab.

### Anatomy

```python
# Basic usage of the Title component
title_component = Title.create("Page Title")
```

### Best Practices

- The `Title` component should be concise but descriptive.
- Each page should have a unique title to facilitate better SEO and usability.