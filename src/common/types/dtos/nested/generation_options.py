from typing import Optional
from pydantic import BaseModel, Field

class GenerationOptions(BaseModel):
    """ Additional configuration options for LLM content generation. """

    seed: Optional[int] = Field(default=None)
    """ [Optional, integer] Random seed used for reproducible outputs """
    
    temperature: Optional[float] = Field(default=None)
    """ [Optional, float] Controls randomness in generation (higher = more random) """

    top_k: Optional[int] = Field(default=None)
    """ [Optional, integer] Limits next token selection to the K most likely """

    top_p: Optional[float] = Field(default=None)
    """ [Optional, float] Cumulative probability threshold for nucleus sampling """

    min_p: Optional[float] = Field(default=None)
    """ [Optional, float] Minimum probability threshold for token selection """

    stop: Optional[str|list[str]] = Field(default=None)
    """ [Optional, string OR string[]] Stop sequences that will halt generation """
    
    num_ctx: Optional[int] = Field(default=None)
    """ [Optional, integer] Context length size """
    
    num_predict: Optional[int] = Field(default=None)
    """ [Optional integer] Maximum number of tokens to generate """
