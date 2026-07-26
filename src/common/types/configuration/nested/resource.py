from pydantic import BaseModel, Field, model_validator
from typing_extensions import Self
from api_provider_details import ApiProviderDetails
from ....utils.text_utils import slugify
from ....enums import ResourceProviderType

class Resource(BaseModel):
    # Required
    display_name: str = Field()
    """ Display name for use by clients and future features """

    slug: str = Field(default_factory=lambda data: slugify(data["display_name"]))
    """ Unique string id, used in API requests """

    # Required
    provider_type: ResourceProviderType = Field()
    """ Provider type, determines detail model """
    
    # Required
    provider_details: ApiProviderDetails = Field()
    """ Detail model dependent on provider type """

    @model_validator(mode='after')
    def check_provider_type_match(self) -> Self:
        """ Ensures that provider_type matches type of provider_details field """

        if self.provider_type == ResourceProviderType.API and not isinstance(self.provider_details, ApiProviderDetails):
            raise ValueError("If 'provider_type' is 'api' then 'provider_details' must match 'ApiProviderDetails' model")
        return self