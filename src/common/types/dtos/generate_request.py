from typing import Optional
from pydantic import BaseModel, Field
from nested.generation_options import GenerationOptions
from ...enums import Format

class GenerateRequest(BaseModel):
    """ Request model for `/generate` API """

    model: str = Field()
    """ [Required, string] Model name """

    prompt: Optional[str] = Field(default=None)
    """ [Optional, string] Text for the model to generate a response from """

    suffix: Optional[str] = Field(default=None)
    """ [Optional, string] Used for fill-in-the-middle models, text that appears after the user prompt and before the model response """

    images: Optional[list[str]] = Field(default=None)
    """ [Optional, string[]] Base64-encoded images for models that support image input """

    format: Optional[Format|dict] = Field(default=None)
    """ [Optional, enum string OR object] Structured output format for the model to generate a response from. Supports either the string `"json"` or a JSON schema object """

    system: Optional[str] = Field(default=None)
    """ [Optional, string] System prompt for the model to generate a response from """

    stream: Optional[bool] = Field(default=None)
    """ [Optional, boolean] When true, returns a stream of partial responses """

    think: Optional[bool] = Field(default=None)
    """ [Optional, boolean] When true, returns separate thinking output in addition to content. Can be a boolean (true/false) or a string ("high", "medium", "low", "max") for supported models, with "max" requesting the highest thinking level. """

    raw: Optional[bool] = Field(default=None)
    """ [Optional, boolean] When true, returns the raw response from the model without any prompt templating """

    keep_alive: Optional[str] = Field(default=None)
    """ [Optional, string] Model keep-alive duration (for example `5m` or `0` to unload immediately) """

    options: Optional[GenerationOptions] = Field(default=None)
    """ [Optional, object] Runtime options that control text generation """

    logprobs: Optional[bool] = Field(default=None)
    """ [Optional, boolean] Whether to return log probabilities of output tokens """

    top_logprobs: Optional[int] = Field(default=None)
    """ [Optional, integer] Number of most likely tokens to return at each position when logprobs are enabled """