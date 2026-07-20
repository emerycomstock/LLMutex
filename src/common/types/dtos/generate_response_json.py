from typing import Optional

from pydantic import BaseModel, Field
from nested.logprobs import Logprobs

class GenerateResponseJson(BaseModel):
    """ Response model for application/json response format for `/generate` API """

    model: str = Field()
    """ Model name """
    
    created_at: str = Field()
    """ ISO 8601 timestamp of response creation """
    
    response: str = Field()
    """ The model's generated text response """
    
    thinking: Optional[str] = Field(default=None)
    """ The model's generated thinking output """
    
    done: bool = Field()
    """ Indicates whether generation has finished """
    
    done_reason: Optional[str] = Field(default=None)
    """ Reason the generation stopped """
    
    total_duration: int = Field()
    """ Time spent generating the response in nanoseconds """
    
    load_duration: int = Field()
    """ Time spend loading the model in nanoseconds """
    
    prompt_eval_count: int = Field()
    """ Number of input tokens in the prompt """
    
    prompt_eval_duration: int = Field()
    """ Time spent evaluating the prompt in nanoseconds """
    
    eval_count: int = Field()
    """ Number of output tokens generated in the response """
    
    eval_duration: int = Field()
    """ Time spent generating tokens in seconds """
    
    logprobs: Optional[list[Logprobs]] = Field(default=None)
    """ Log probability infromation for the generated tokens where logprobs are enabled """
    