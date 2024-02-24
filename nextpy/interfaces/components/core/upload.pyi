# This file has been modified by the Nextpy Team in 2023 using AI tools and automation scripts. 
# We have rigorously tested these modifications to ensure reliability and performance. Based on successful test results, we are confident in the quality and stability of these changes.

"""Stub file for nextpy/components/core/upload.py"""
# ------------------- DO NOT EDIT ----------------------
# This file was generated by `scripts/pyi_generator.py`!
# ------------------------------------------------------

from typing import Any, Dict, Literal, Optional, Union, overload
from nextpy.backend.vars import Var, BaseVar, ComputedVar
from nextpy.backend.event import EventChain, EventHandler, EventSpec
from nextpy.interfaces.web.style import Style
from typing import Any, Dict, List, Optional, Union
from nextpy import constants
from nextpy.interfaces.web.components.chakra.forms.input import Input
from nextpy.interfaces.web.components.chakra.layout.box import Box
from nextpy.interfaces.web.components.component import Component
from nextpy.constants import Dirs
from nextpy.backend.event import CallableEventSpec, EventChain, EventSpec, call_script
from nextpy.frontend import imports
from nextpy.backend.vars import BaseVar, CallableVar, Var, VarData

DEFAULT_UPLOAD_ID: str
upload_files_context_var_data: VarData

@CallableVar
def upload_file(id_: str = DEFAULT_UPLOAD_ID) -> BaseVar: ...
@CallableVar
def selected_files(id_: str = DEFAULT_UPLOAD_ID) -> BaseVar: ...
@CallableEventSpec
def clear_selected_files(id_: str = DEFAULT_UPLOAD_ID) -> EventSpec: ...
def cancel_upload(upload_id: str) -> EventSpec: ...

class UploadFilesProvider(Component):
    @overload
    @classmethod
    def create(  # type: ignore
        cls,
        *children,
        style: Optional[Style] = None,
        key: Optional[Any] = None,
        id: Optional[Any] = None,
        class_name: Optional[Any] = None,
        autofocus: Optional[bool] = None,
        custom_attrs: Optional[Dict[str, Union[Var, str]]] = None,
        on_blur: Optional[
            Union[EventHandler, EventSpec, list, function, BaseVar]
        ] = None,
        on_click: Optional[
            Union[EventHandler, EventSpec, list, function, BaseVar]
        ] = None,
        on_context_menu: Optional[
            Union[EventHandler, EventSpec, list, function, BaseVar]
        ] = None,
        on_double_click: Optional[
            Union[EventHandler, EventSpec, list, function, BaseVar]
        ] = None,
        on_focus: Optional[
            Union[EventHandler, EventSpec, list, function, BaseVar]
        ] = None,
        on_mount: Optional[
            Union[EventHandler, EventSpec, list, function, BaseVar]
        ] = None,
        on_mouse_down: Optional[
            Union[EventHandler, EventSpec, list, function, BaseVar]
        ] = None,
        on_mouse_enter: Optional[
            Union[EventHandler, EventSpec, list, function, BaseVar]
        ] = None,
        on_mouse_leave: Optional[
            Union[EventHandler, EventSpec, list, function, BaseVar]
        ] = None,
        on_mouse_move: Optional[
            Union[EventHandler, EventSpec, list, function, BaseVar]
        ] = None,
        on_mouse_out: Optional[
            Union[EventHandler, EventSpec, list, function, BaseVar]
        ] = None,
        on_mouse_over: Optional[
            Union[EventHandler, EventSpec, list, function, BaseVar]
        ] = None,
        on_mouse_up: Optional[
            Union[EventHandler, EventSpec, list, function, BaseVar]
        ] = None,
        on_scroll: Optional[
            Union[EventHandler, EventSpec, list, function, BaseVar]
        ] = None,
        on_unmount: Optional[
            Union[EventHandler, EventSpec, list, function, BaseVar]
        ] = None,
        **props
    ) -> "UploadFilesProvider":
        """Create the component.

        Args:
            *children: The children of the component.
            style: The style of the component.
            key: A unique key for the component.
            id: The id for the component.
            class_name: The class name for the component.
            autofocus: Whether the component should take the focus once the page is loaded
            custom_attrs: custom attribute
            **props: The props of the component.

        Returns:
            The component.

        Raises:
            TypeError: If an invalid child is passed.
        """
        ...

class Upload(Component):
    @overload
    @classmethod
    def create(  # type: ignore
        cls,
        *children,
        accept: Optional[
            Union[Var[Optional[Dict[str, List]]], Optional[Dict[str, List]]]
        ] = None,
        disabled: Optional[Union[Var[bool], bool]] = None,
        max_files: Optional[Union[Var[int], int]] = None,
        max_size: Optional[Union[Var[int], int]] = None,
        min_size: Optional[Union[Var[int], int]] = None,
        multiple: Optional[Union[Var[bool], bool]] = None,
        no_click: Optional[Union[Var[bool], bool]] = None,
        no_drag: Optional[Union[Var[bool], bool]] = None,
        no_keyboard: Optional[Union[Var[bool], bool]] = None,
        style: Optional[Style] = None,
        key: Optional[Any] = None,
        id: Optional[Any] = None,
        class_name: Optional[Any] = None,
        autofocus: Optional[bool] = None,
        custom_attrs: Optional[Dict[str, Union[Var, str]]] = None,
        on_blur: Optional[
            Union[EventHandler, EventSpec, list, function, BaseVar]
        ] = None,
        on_click: Optional[
            Union[EventHandler, EventSpec, list, function, BaseVar]
        ] = None,
        on_context_menu: Optional[
            Union[EventHandler, EventSpec, list, function, BaseVar]
        ] = None,
        on_double_click: Optional[
            Union[EventHandler, EventSpec, list, function, BaseVar]
        ] = None,
        on_drop: Optional[
            Union[EventHandler, EventSpec, list, function, BaseVar]
        ] = None,
        on_focus: Optional[
            Union[EventHandler, EventSpec, list, function, BaseVar]
        ] = None,
        on_mount: Optional[
            Union[EventHandler, EventSpec, list, function, BaseVar]
        ] = None,
        on_mouse_down: Optional[
            Union[EventHandler, EventSpec, list, function, BaseVar]
        ] = None,
        on_mouse_enter: Optional[
            Union[EventHandler, EventSpec, list, function, BaseVar]
        ] = None,
        on_mouse_leave: Optional[
            Union[EventHandler, EventSpec, list, function, BaseVar]
        ] = None,
        on_mouse_move: Optional[
            Union[EventHandler, EventSpec, list, function, BaseVar]
        ] = None,
        on_mouse_out: Optional[
            Union[EventHandler, EventSpec, list, function, BaseVar]
        ] = None,
        on_mouse_over: Optional[
            Union[EventHandler, EventSpec, list, function, BaseVar]
        ] = None,
        on_mouse_up: Optional[
            Union[EventHandler, EventSpec, list, function, BaseVar]
        ] = None,
        on_scroll: Optional[
            Union[EventHandler, EventSpec, list, function, BaseVar]
        ] = None,
        on_unmount: Optional[
            Union[EventHandler, EventSpec, list, function, BaseVar]
        ] = None,
        **props
    ) -> "Upload":
        """Create an upload component.

        Args:
            *children: The children of the component.
            accept: The list of accepted file types. This should be a dictionary of MIME types as keys and array of file formats as  values.  supported MIME types: https://developer.mozilla.org/en-US/docs/Web/HTTP/Basics_of_HTTP/MIME_types/Common_types
            disabled: Whether the dropzone is disabled.
            max_files: The maximum number of files that can be uploaded.
            max_size: The maximum file size (bytes) that can be uploaded.
            min_size: The minimum file size (bytes) that can be uploaded.
            multiple: Whether to allow multiple files to be uploaded.
            no_click: Whether to disable click to upload.
            no_drag: Whether to disable drag and drop.
            no_keyboard: Whether to disable using the space/enter keys to upload.
            style: The style of the component.
            key: A unique key for the component.
            id: The id for the component.
            class_name: The class name for the component.
            autofocus: Whether the component should take the focus once the page is loaded
            custom_attrs: custom attribute
            **props: The properties of the component.

        Returns:
            The upload component.
        """
        ...
    def get_event_triggers(self) -> dict[str, Union[Var, Any]]: ...
