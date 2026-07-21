from typing import Optional

from pydantic import BaseModel, Field
from ....enums import ToolType

class ToolDefFunction(BaseModel):
    """ Details about a tool definition """

    name: str = Field()
    """ [Required, string] Name of the function to call """

    description: Optional[str] = Field(default=None)
    """ [Optional, string] What the function does """

    parameters: dict = Field()
    """ [Required, object] JSON Schema for the function parameters """

class ToolDef(BaseModel):
    """ Wrapper over details about a tool definition """

    type: ToolType = Field()
    """ [Required, enum string] Type of tool (always `function`) """

    function: ToolDefFunction = Field()
    """ [Required, object] Function definition """