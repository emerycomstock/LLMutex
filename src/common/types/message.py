from pydantic import BaseModel
from tool_call import ToolCall
from ..enums import Role

class Message(BaseModel):
    """ A single message in the chat history """

    role: Role
    """ [Required, enum string] Author of the message """
    
    content: str
    """ [Required, string] Message text content """
    
    images: list[str]
    """ [Optional, string[]] List of base64-encoded inline images for multimodal models """

    tool_calls: list[ToolCall]
    """ [Optional, object[]] Tool call requests produced by the model """