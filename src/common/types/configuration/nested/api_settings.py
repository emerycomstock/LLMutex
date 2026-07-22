from pydantic import BaseModel, Field

class APISettings(BaseModel):
    http_port: int = Field(default=3440)
    """ HTTP port the server runs on """