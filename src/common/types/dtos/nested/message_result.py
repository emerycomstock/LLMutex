from typing import Optional
from pydantic import BaseModel, Field
from message import Message
from tool_call import ToolCall
from ....enums import Role

class MessageResult(BaseModel):
    """ A message result returned by the model """

    role: Role = Field()
    """ Author of the message """
    
    content: str = Field()
    """ Message text content """

    thinking: Optional[str] = Field(default=None)
    """ Optional deliberate thinking trace when think is enabled """
    
    images: Optional[list[str]] = Field(default=None)
    """ List of base64-encoded inline images for multimodal models """

    tool_calls: Optional[list[ToolCall]] = Field(default=None)
    """ Tool call requests produced by the model """

    def to_message(self) -> Message:
        return Message(self.role, self.content, self.images, self.tool_calls)