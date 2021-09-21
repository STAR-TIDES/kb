'''star_tides.core.actions.delete_project_action
'''
from mongoengine.errors import DoesNotExist
from star_tides.core.actions.base_action import Action
from star_tides.services.databases.mongo.models.project_model import ProjectModel
from star_tides.exceptions import NotFoundError


class DeleteProjectAction(Action):
    def __init__(self, project_id: str) -> None:
        self.project_id = project_id

    def run(self) -> None:
        try:
            ProjectModel.objects.get(id=self.project_id).delete()
        except DoesNotExist as e:
            raise NotFoundError(
                f'Could not find project with ID {self.project_id}.') from e
