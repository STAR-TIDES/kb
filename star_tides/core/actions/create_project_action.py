'''star_tides.core.actions.create_project_action
'''

from star_tides.services.databases.mongo.schemas.project_schema import ProjectSchema
from star_tides.services.databases.mongo.models.project_model import ProjectModel
from star_tides.core.actions.base_action import Action
from star_tides.exceptions import InvalidParamError
from star_tides.core.data.project_data import ProjectData


class CreateProjectAction(Action):
    def __init__(self, project: ProjectData) -> None:
        self.project = project

    def run(self):
        if self.project.id is not None:
            raise InvalidParamError('Expected project not to have ID.')
        schema = ProjectSchema().load(self.contact._asdict())
        saved_model = ProjectModel(**schema, _created=True).save()
        return ProjectData.from_model(saved_model)
