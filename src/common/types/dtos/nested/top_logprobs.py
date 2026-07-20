from pydantic import BaseModel, Field

class TopLogprobs(BaseModel):
    """ Item included as part of top logprobs collection """

    token: str = Field()
    """ The text representation of the token """

    logprob: int = Field()
    """ The log probability of this token """

    bytes: list[int] = Field()
    """ The raw byte representation of the token """