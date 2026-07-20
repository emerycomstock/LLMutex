from typing import Optional
from pydantic import BaseModel, Field
from ..message import Message
from ..tool_def import ToolDef
from ..generation_options import GenerationOptions
from ...enums import Format

class ChatRequest(BaseModel):
    model: str = Field()
    """ [Required, string] model name """

    messages: list[Message] = Field()
    """ [Required, object[]] Chat history as an array of message objects (each with a role and content) """

    tools: Optional[list[ToolDef]] = Field(default=None)
    """ [Optional, object[]] Optional list of function tools the model may call during the chat """

    format: Optional[Format] = Field(default=None)
    """ [Optional, enum string OR object] Structured output format for the model to generate a response from. Supports either the string `"json"` or a JSON schema object """

    stream: Optional[bool] = Field(default=None)
    """ [Optional, boolean] When true, returns a stream of partial responses """

    think: Optional[bool] = Field(default=None)
    """ [Optional, boolean] When true, returns separate thinking output in addition to content. Can be a boolean (true/false) or a string ("high", "medium", "low", "max") for supported models, with "max" requesting the highest thinking level. """

    keep_alive: Optional[str] = Field(default=None)
    """ [Optional, string] Model keep-alive duration (for example `5m` or `0` to unload immediately) """

    options: Optional[GenerationOptions] = Field(default=None)
    """ [Optional, object] Runtime options that control text generation """

    logprobs: Optional[bool] = Field(default=None)
    """ [Optional, boolean] Whether to return log probabilities of output tokens """

    top_logprobs: Optional[int] = Field(default=None)
    """ [Optional, integer] Number of most likely tokens to return at each position when logprobs are enabled """
