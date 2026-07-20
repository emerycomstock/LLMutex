from pydantic import BaseModel
from ..generation_options import GenerationOptions
from ...enums import Format

class GenerateRequest(BaseModel):
    model: str
    """ [Required, string] Model name """

    prompt: str
    """ [Optional, string] Text for the model to generate a response from """

    suffix: str
    """ [Optional, string] Used for fill-in-the-middle models, text that appears after the user prompt and before the model response """

    images: list[str]
    """ [Optional, string[]] Base64-encoded images for models that support image input """

    format: Format|object
    """ [Optional, enum string OR object] Structured output format for the model to generate a response from. Supports either the string `"json"` or a JSON schema object """

    system: str
    """ [Optional, string] System prompt for the model to generate a response from """

    stream: bool
    """ [Optional, boolean] When true, returns a stream of partial responses """

    think: bool
    """ [Optional, boolean] When true, returns separate thinking output in addition to content. Can be a boolean (true/false) or a string ("high", "medium", "low", "max") for supported models, with "max" requesting the highest thinking level. """

    raw: bool
    """ [Optional, boolean] When true, returns the raw response from the model without any prompt templating """

    keep_alive: str
    """ [Optional, string] Model keep-alive duration (for example `5m` or `0` to unload immediately) """

    options: GenerationOptions
    """ [Optional, object] Runtime options that control text generation """

    logprobs: bool
    """ [Optional, boolean] Whether to return log probabilities of output tokens """

    top_logprobs: int
    """ [Optional, integer] Number of most likely tokens to return at each position when logprobs are enabled """