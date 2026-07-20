from typing import Optional
from pydantic import BaseModel, Field

class ToolCallFunction(BaseModel):
    """ Details about a tool call requested by an agent """

    name: str = Field()
    """ [Required, string] Name of the function to call """

    description: Optional[str] = Field(default=None)
    """ [Optional, string] What the function does """

    arguments: Optional[dict] = Field(default=None)
    """ [Optional, object] JSON object of arguments to pass the function """

class ToolCall(BaseModel):
    """ Wrapper over details about a tool call requested by the agent """

    function: ToolCallFunction = Field()
    """ [Required, object] Function definition """