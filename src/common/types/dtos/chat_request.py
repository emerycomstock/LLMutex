from pydantic import BaseModel
from ..message import Message
from ..tool_def import ToolDef
from ..generation_options import GenerationOptions
from ...enums import Format

class ChatRequest(BaseModel):
    model: str
    """ [Required, string] model name """

    messages: list[Message]
    """ [Required, object[]] Chat history as an array of message objects (each with a role and content) """

    tools: list[ToolDef]
    """ [Optional, object[]] Optional list of function tools the model may call during the chat """

    format: Format
    """ [Optional, enum string OR object] Structured output format for the model to generate a response from. Supports either the string `"json"` or a JSON schema object """

    stream: bool
    """ [Optional, boolean] When true, returns a stream of partial responses """

    think: bool
    """ [Optional, boolean] When true, returns separate thinking output in addition to content. Can be a boolean (true/false) or a string ("high", "medium", "low", "max") for supported models, with "max" requesting the highest thinking level. """

    keep_alive: str
    """ [Optional, string] Model keep-alive duration (for example `5m` or `0` to unload immediately) """

    options: GenerationOptions
    """ [Optional, object] Runtime options that control text generation """

    logprobs: bool
    """ [Optional, boolean] Whether to return log probabilities of output tokens """

    top_logprobs: int
    """ [Optional, integer] Number of most likely tokens to return at each position when logprobs are enabled """
