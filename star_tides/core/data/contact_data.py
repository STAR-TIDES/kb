'''star_tides.core.data.contact_data
'''

from star_tides.services.databases.mongo.models.contact_model import ContactModel
from star_tides.services.databases.mongo.schemas.contact_schema import ContactSchema
from star_tides.services.databases.mongo.models.availability import Availability
from star_tides.core.data.location_data import LocationData
from star_tides.core.data.engagement_data import EngagementData
from typing import List, NamedTuple, Optional

class ContactData(NamedTuple):
    '''ContactData represents a Contact object's data in our system.'''

    user_id: Optional[str]
    name: str
    email: Optional[str]
    phone_number: Optional[str]
    job_title: Optional[str]
    website_url: Optional[str]
    location: LocationData
    languages: List[str]
    availability: Availability
    engagement: EngagementData
    statuses: List[str]

    @staticmethod
    def from_model(model: ContactModel):
        return ContactData(**(ContactSchema().dump(model)))
