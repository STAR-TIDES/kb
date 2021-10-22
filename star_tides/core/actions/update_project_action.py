'''star_tides.core.actions.update_project_action
'''

from star_tides.services.databases.mongo.schemas.project_schema import ProjectSchema
from star_tides.services.databases.mongo.models.project_model import ProjectModel
from star_tides.core.data.project_data import ProjectData
from star_tides.core.actions.get_project_action import GetProjectAction
from star_tides.core.actions.base_action import Action


class UpdateProjectAction(Action):
    '''UpdateProjectAction updates a Project in the database using the given
    Project ID and update dictionary.
    '''

    def __init__(self, project_id: str, updates: dict) -> None:
        self.project_id = project_id
        self.updates = updates

    def run(self) -> ProjectData:
        # TODO(ljr): Add update_timestamps.
        old_project = GetProjectAction(self.project_id).run()
        merged_project = old_project._replace(**self.updates)
        schema = ProjectSchema(partial=True).load(merged_project._asdict())
        updated_model = ProjectModel.objects(
            id=self.project_id).modify(**schema, new=True)
        return ProjectData.from_model(updated_model)
