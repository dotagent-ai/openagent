##  Reference for nextpy/frontend/components/react_player/video.pyi

# Video Component

The `Video` component in Nextpy is an extension of the `ReactPlayer` component, designed to embed and control video playback in your Nextpy application.

## Overview

The `Video` component offers a range of functionalities, including playing, pausing, looping videos, and displaying native player controls. It is highly customizable and can be integrated into any part of your Nextpy application where video playback is required.

## Use Cases

- Embedding instructional videos in educational platforms.
- Incorporating product videos in e-commerce sites.
- Building a media player for a video streaming service.
- Displaying promotional content on a landing page.

## Anatomy

To use the `Video` component, import it from the `nextpy.components.react_player.video` module and use the `create` class method to instantiate it.

### Basic Example

```python
from nextpy.components.react_player.video import Video

video_component = Video.create(
    url="http://commondatastorage.googleapis.com/gtv-videos-bucket/sample/BigBuckBunny.mp4",
    playing=True,
    controls=True,
    width="640",
    height="360"
)
```

### Advanced Example

For a more advanced setup, you can control the video programmatically using reactive variables and handle various events.

```python
from nextpy import Var
from nextpy.components.react_player.video import Video

url_var = Var("http://commondatastorage.googleapis.com/gtv-videos-bucket/sample/BigBuckBunny.mp4")
playing_var = Var(False)

video_component = Video.create(
    url=url_var,
    playing=playing_var,
    loop=True,
    controls=True,
    on_click=lambda: playing_var.set(not playing_var.get())
)
```

## Components

- `url`: The URL of a video to play.
- `playing`: Controls playback state.
- `loop`: Determines if the video should loop.
- `controls`: Toggles the visibility of native player controls.
- `light`: Enables a thumbnail preview mode.
- `volume`: Adjusts the volume level.
- `muted`: Mutes the video.
- `width`: Sets the width of the player.
- `height`: Sets the height of the player.

## Notes

- Ensure that the video URL is accessible and points to a supported video format.
- Be mindful of the autoplay policies in modern browsers that might prevent videos from playing automatically.
- Volume control might not work on all mobile devices due to restrictions in the mobile operating system.

## Best Practices

- When embedding videos, consider lazy loading them to improve page load times.
- Always provide controls for the user to play, pause, or stop the video.
- If the video is not essential to your application, make sure it does not auto-play with sound, as this can be intrusive.
- Use the `light` mode to save bandwidth and improve load times, especially for users on slower connections.

By following these guidelines, developers can effectively utilize the `Video` component within Nextpy applications, providing users with a seamless video playback experience.