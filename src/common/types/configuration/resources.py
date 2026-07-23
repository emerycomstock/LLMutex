from pydantic import BaseModel, Field
from nested.api_provider_details import ApiProviderDetails
from ...enums import ResourceProviderType

class Resources(BaseModel):
    id: str = Field()
    """ Unique string id, used in API requests """
    
    display_name: str = Field()
    """ Display name for use by clients and future features """

    provider_type: ResourceProviderType = Field()
    """ Provider type, determines detail model """
    
    provider_details: ApiProviderDetails = Field()
    """ Detail model dependent on provider type """

    # TODO: Validation for provider_type -> provider_details type match