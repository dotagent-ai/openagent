# This file has been modified by the Nextpy Team in 2023 using AI tools and automation scripts. 
# We have rigorously tested these modifications to ensure reliability and performance. Based on successful test results, we are confident in the quality and stability of these changes.

"""A date input component."""

from nextpy.backend.vars import Var
from nextpy.interfaces.web.components.chakra.forms.input import Input


class DatePicker(Input):
    """A date input component."""

    # The type of input.
    type_: Var[str] = "date"  # type: ignore
