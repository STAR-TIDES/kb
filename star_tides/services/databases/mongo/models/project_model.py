'''star_tides.services.databases.mongo.models.project_model
'''

from star_tides.services.databases.mongo.models.project_status import ProjectStatus
from star_tides.services.databases.mongo.models.engagement_model import EngagementModel
from star_tides.services.databases.mongo.models.location_model import LocationModel
from star_tides.services.databases.mongo.models.update_model import UpdateModel
from mongoengine.document import Document
from mongoengine.fields import EmbeddedDocumentField, EmbeddedDocumentListField, EnumField, ListField, StringField, ObjectIdField


class ProjectModel(Document):
    '''Project represents a project in the STAR-TIDES network.
    '''
    name = StringField(required=True)
    location = EmbeddedDocumentField(LocationModel, required=True)
    engagement = EmbeddedDocumentField(EngagementModel, required=True)
    contacts = ListField(ObjectIdField, required=False)
    summary = StringField(required=True)
    # For now, we will just refer to grants by their name or URL.
    # In the future, we may have grant objects in our DB and can reference them
    # by ObjectId.
    grants = ListField(StringField, required=False)
    solution_costs = StringField(required=False)
    updates = EmbeddedDocumentListField(UpdateModel, required=True)
    notes = StringField(required=False)
    # TODO(ljr): Add ListField(ObjectIdField) for guides
    # once we have the model for those.
    status = EnumField(ProjectStatus, required=True)
