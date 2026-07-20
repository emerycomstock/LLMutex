from pydantic import BaseModel

class ChatResponseNdjson(BaseModel):
    """ Response model for application/x-ndjson response format for `/chat` API """
    pass
