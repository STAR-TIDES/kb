'''star_tides.core.data.contact_data
'''


from star_tides.services.databases.mongo.models.contact_model import ContactModel
from star_tides.services.databases.mongo.models.availability import Availability
from star_tides.core.data.location_data import LocationData
from star_tides.core.data.engagement_data import EngagementData
from typing import List, NamedTuple, Optional


class ContactData(NamedTuple):
    '''ContactData represents a Contact object's data in our system.'''
    # Fields with NO default values.
    name: str
    location: LocationData
    availability: Availability
    engagement: EngagementData
    # Fields with default values.
    id: Optional[str] = None
    user_id: Optional[str] = None
    email: Optional[str] = None
    phone_number: Optional[str] = None
    job_title: Optional[str] = None
    website_url: Optional[str] = None
    languages: List[str] = []
    statuses: List[str] = []
    # TODO(i/15): Include this back in once update_timestamps works in
    # ContactSchema.
    # update_timestamps: List[UpdateTimestampData] = []

    @staticmethod
    def from_model(model: ContactModel):
        d = model.to_mongo()
        del d['_id']
        d['id'] = str(model.id)

        return ContactData(**d)
