from pydantic import BaseModel

class GenerationOptions(BaseModel):
    """ Additional configuration options for LLM content generation. """

    seed: int
    """ [Optional, integer] Random seed used for reproducible outputs """
    
    temperature: float
    """ [Optional, float] Controls randomness in generation (higher = more random) """

    top_k: int
    """ [Optional, integer] Limits next token selection to the K most likely """

    top_p: float
    """ [Optional, float] Cumulative probability threshold for nucleus sampling """

    min_p: float
    """ [Optional, float] Minimum probability threshold for token selection """

    stop: str|list[str]
    """ [Optional, string OR string[]] Stop sequences that will halt generation """
    
    num_ctx: int
    """ [Optional, integer] Context length size """
    
    num_predict: int
    """ [Optional integer] Maximum number of tokens to generate """
