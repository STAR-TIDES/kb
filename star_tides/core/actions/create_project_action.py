'''star_tides.core.actions.create_project_action
'''

from marshmallow.exceptions import ValidationError
from star_tides.services.databases.mongo.schemas.project_schema import ProjectSchema
from star_tides.services.databases.mongo.models.project_model import ProjectModel
from star_tides.core.actions.base_action import Action
from star_tides.exceptions import InvalidParamError
from star_tides.core.data.project_data import ProjectData


class CreateProjectAction(Action):
    '''Action that creates a Project document in the DB given a ProjectData.'''

    def __init__(self, project: ProjectData) -> None:
        self.project = project

    def run(self):
        if self.project.id is not None:
            raise InvalidParamError('Expected project not to have ID.')
        schema = {}
        try:
            schema = ProjectSchema().load(self.project._asdict())
        except ValidationError as e:
            raise InvalidParamError(
                f'Failed to validate using schema: {e.messages}') from e
        saved_model = ProjectModel(**schema, _created=True).save()
        return ProjectData.from_model(saved_model)
