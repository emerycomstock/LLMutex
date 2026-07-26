from pydantic import BaseModel, Field
from nested.resource import Resource

class Resources(BaseModel):
    resources: list[Resource] = Field(default=[])
    """ Collection of resource entries """