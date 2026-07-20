from pydantic import BaseModel

class ToolCallFunction(BaseModel):
    """ Details about a tool call requested by an agent """

    name: str
    """ [Required, string] Name of the function to call """

    description: str
    """ [Optional, string] What the function does """

    arguments: dict
    """ [Optional, object] JSON object of arguments to pass the function """

class ToolCall(BaseModel):
    """ Wrapper over details about a tool call requested by the agent """

    function: ToolCallFunction
    """ [Required, object] Function definition """