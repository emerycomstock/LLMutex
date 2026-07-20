from typing import Optional

from pydantic import BaseModel, Field
from tool_call import ToolCall
from ..enums import Role

class Message(BaseModel):
    """ A single message in the chat history """

    role: Role = Field()
    """ [Required, enum string] Author of the message """
    
    content: str = Field()
    """ [Required, string] Message text content """
    
    images: Optional[list[str]] = Field(default=None)
    """ [Optional, string[]] List of base64-encoded inline images for multimodal models """

    tool_calls: Optional[list[ToolCall]] = Field(default=None)
    """ [Optional, object[]] Tool call requests produced by the model """