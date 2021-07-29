'''star_tides.core.data.project_data
'''
from typing import NamedTuple, Text, List, Optional
from star_tides.core.data.location_data import LocationData
from star_tides.core.data.engagement_data import EngagementData
from star_tides.services.databases.mongo.models.project_status import ProjectStatus
from star_tides.services.databases.mongo.models.project_model import ProjectModel
from star_tides.core.data.update_data import UpdateData


class ProjectData(NamedTuple):
    '''ProjectData represents a Project object's data in our system.'''
    name: Text
    location: LocationData
    engagement: EngagementData
    summary: Text
    updates: List[UpdateData]
    status: ProjectStatus

    id: Optional[str] = None
    contacts: List[str] = []
    grants: List[str] = []
    solution_costs: Optional[Text] = None
    notes: Optional[Text] = None

    @ staticmethod
    def from_model(model: ProjectModel):
        d = model.to_mongo()
        del d['_id']
        d['id'] = str(model.id)
        return ProjectData(**d)
