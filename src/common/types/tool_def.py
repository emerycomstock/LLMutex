from pydantic import BaseModel
from ..enums import ToolType

class ToolDefFunction(BaseModel):
    """ Details about a tool definition """

    name: str
    """ [Required, string] Name of the function to call """

    description: str
    """ [Optional, string] What the function does """

    parameters: dict
    """ [Required, object] JSON Schema for the function parameters """

class ToolDef(BaseModel):
    """ Wrapper over details about a tool definition """

    type: ToolType
    """ [Required, enum string] Type of tool (always `function`) """

    function: ToolDefFunction
    """ [Required, object] Function definition """