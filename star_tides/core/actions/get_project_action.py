'''star_tides.core.action.get_project_action
'''
from mongoengine.errors import DoesNotExist
from star_tides.exceptions import NotFoundError
from star_tides.core.actions.base_action import Action
from star_tides.core.data.project_data import ProjectData
from star_tides.services.databases.mongo.models.project_model import ProjectModel


class GetProjectAction(Action):
    '''Fetches a ProjectData from the database using the given project ID.'''

    def __init__(self, project_id: str) -> None:
        self.project_id = project_id

    def run(self):
        try:
            model = ProjectModel.objects.get(id=self.project_id)
        except DoesNotExist as e:
            raise NotFoundError(
                f'Could not find project with ID {self.project_id}.'
            ) from e
        return ProjectData.from_model(model)
