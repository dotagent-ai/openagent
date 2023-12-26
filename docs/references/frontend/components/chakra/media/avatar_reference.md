##  Reference for nextpy/frontend/components/chakra/media/avatar.pyi

# Nextpy Documentation: Avatar Component

## Avatar

### Overview

The `Avatar` component is used to display an individual user's profile picture. This can represent a person or an entity and is typically used in user interfaces where user identity is essential, such as in messaging apps, comment threads, or social media timelines.

### Purpose

The purpose of the `Avatar` component is to visually represent a user with a picture or a placeholder icon when the image is not available.

### Use Cases

- Displaying user profiles in an application's user interface.
- Showing who is currently logged in or active within an application.
- Providing a visual cue in comment sections to distinguish between different commenters.
- Integrating into user lists or contact lists to show images alongside user information.

### Anatomy

The `Avatar` component has the following structure:

```python
Avatar.create(
    icon="path/to/default/icon.svg",
    name="John Doe",
    src="path/to/user/image.jpg",
    size="md",
    style=Style(...),
    on_click=handle_click_event
)
```

#### Basic Example

```python
avatar = Avatar.create(
    name="John Doe",
    src="http://example.com/johndoe.jpg",
    size="md"
)
```

#### Advanced Example

```python
avatar_with_event = Avatar.create(
    name="Jane Doe",
    src="http://example.com/janedoe.jpg",
    size="lg",
    on_click=lambda event: print("Avatar clicked")
)
```

### Components

The `Avatar` component can include sub-components like `AvatarBadge` and can be part of an `AvatarGroup`.

#### AvatarBadge

A sub-component that is typically used to show the status of the user (online, offline, busy, etc.).

#### AvatarGroup

This component is used to stack multiple `Avatar` components together, often used to show a group of users.

#### Properties Table

| Prop Name         | Type   | Description                                                  |
|-------------------|--------|--------------------------------------------------------------|
| `icon`            | string | The default avatar used as fallback when no image is present.|
| `icon_label`      | string | The label for the icon used for accessibility purposes.      |
| `ignore_fallback` | bool   | If true, always use the `img` element, ignoring fallback.    |
| `name`            | string | The name of the person displayed by the avatar.              |
| `show_border`     | bool   | If true, display a border around the avatar.                 |
| `src`             | string | The URL of the avatar image.                                 |
| `src_set`         | string | List of sources for different screen resolutions.            |
| `size`            | enum   | Preset sizes for the avatar: "2xs", "xs", "sm", etc.         |
| `style`           | Style  | Custom styles to apply to the avatar.                        |

#### Event Triggers

- `on_click`: Event fired when the avatar is clicked.
- `on_error`: Event fired if there is an error loading the avatar image.
- `on_mouse_enter`: Event fired when the mouse enters the avatar area.
- `on_mouse_leave`: Event fired when the mouse leaves the avatar area.

### Notes

- If the `src` attribute is not provided, the avatar will display the `icon` or the initials from the `name` prop.
- The `size` prop allows for predefined sizes but can also be customized using the `style` prop.

### Best Practices

- Use appropriate sizes (`size` prop) for different contexts; smaller avatars for lists and larger ones for profile views.
- Always provide an `icon` or `icon_label` for accessibility and as a fallback when the image source is not available.
- Utilize the `AvatarGroup` to neatly display a collection of avatars with proper spacing and maximum number visible.

---

This documentation ensures developers have the necessary information to implement the `Avatar` component effectively within their applications, with examples and best practices to guide them.