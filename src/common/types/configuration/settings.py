from pydantic import BaseModel, Field
from nested.api_settings import APISettings

class Settings(BaseModel):
    api: APISettings = Field(default=APISettings())
    """ API settings """