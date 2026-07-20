from pydantic import BaseModel, Field
from llmutex.src.common.types.dtos.nested.top_logprobs import TopLogprobs

class Logprobs(BaseModel):
    """ Item included in logprobs collection """

    token: str = Field()
    """ The text representation of the token """
    
    logprob: int = Field()
    """ The log probability of this token """
    
    bytes: list[int] = Field()
    """ The raw byte representation of the token """
    
    top_logprobs: list[TopLogprobs] = Field()
    """ Most likely tokens and their log probabilities at this position """
    