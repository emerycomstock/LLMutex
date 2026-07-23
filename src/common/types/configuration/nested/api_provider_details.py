from pydantic import BaseModel, Field
from ....enums import ApiResourceSpec
from ....constants import MIN_PORT, MAX_PORT

class ApiProviderDetails(BaseModel):

    spec: ApiResourceSpec = Field()
    """ API spec for resource """

    host: str = Field()
    """ Host name or address for invoking API resource (i.e. localhost) """

    port: int = Field(min=MIN_PORT, max=MAX_PORT)
    """ Port API resource is accessible on (i.e. 11434 for Ollama) """
