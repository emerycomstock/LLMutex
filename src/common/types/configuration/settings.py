from pydantic import BaseModel, Field
from nested.api_settings import APISettings

# TODO: Defaults and default factories
class Settings(BaseModel):
    api: APISettings = Field(default=APISettings())
    """ API settings """