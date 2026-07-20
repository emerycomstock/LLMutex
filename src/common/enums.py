from enum import Enum

class Role(str, Enum):
    SYSTEM = "system",
    USER = "user",
    ASSISTANT = "assistant",
    TOOL = "tool"
    
class Format(str, Enum):
    JSON = "json"

class ToolType(str, Enum):
    FUNCTION = "function"

class ResponseType(str, Enum):
    JSON = "json"
    JSON_STREAM = "json-stream"
    UNSUPPORTED = "unsupported"