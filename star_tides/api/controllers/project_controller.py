'''star_tides.api.controllers.project_controller
'''

from star_tides.services.databases.mongo.schemas.project_schema import ProjectSchema
from star_tides.core.data.project_data import ProjectData
from star_tides.core.actions.update_project_action import UpdateProjectAction
from star_tides.core.actions.delete_project_action import DeleteProjectAction
from star_tides.core.actions.create_project_action import CreateProjectAction
from star_tides.core.actions.list_projects_action import ListProjectsAction
from star_tides.api.controllers.base_controller import Controller
from star_tides.api.controllers import snake_case_dict, validate_document_id
from star_tides.core.actions.get_project_action import GetProjectAction
from star_tides.exceptions import InvalidParamError


class ListProjectsController(Controller):
    def process_request(self) -> dict:
        projects = ListProjectsAction().run()
        return {
            'projects': [project._asdict() for project in projects]
        }


class GetProjectController(Controller):
    def __init__(self, project_id: str) -> None:
        self.project_id = project_id

    def process_request(self):
        validate_document_id(self.project_id)
        project = GetProjectAction(self.project_id).run()
        return project._asdict()


class CreateProjectController(Controller):
    def process_request(self):
        body = self.get_request_body()
        if not body:
            raise InvalidParamError('Expected JSON body to be present.')
        json_body = snake_case_dict(body)
        ProjectSchema().validate(json_body)
        parsed_project = ProjectData(**json_body)
        created_project = CreateProjectAction(parsed_project).run()
        return created_project._asdict()


class DeleteProjectController(Controller):
    def __init__(self, project_id: str) -> None:
        self.project_id = project_id

    def process_request(self):
        validate_document_id(self.project_id)
        DeleteProjectAction(self.project_id).run()
        return {}


class UpdateProjectController(Controller):
    '''UpdateProjectController takes an existing Project ID and an update JSON
    payload from the request body and updates the corresponding Project in the
    database.
    '''

    def __init__(self, project_id) -> None:
        self.project_id = project_id

    def process_request(self):
        validate_document_id(self.project_id)
        body = self.get_request_body()
        if not body:
            raise InvalidParamError('Expected JSON body to be present.')
        json_body = snake_case_dict(body)
        updated_project = UpdateProjectAction(self.project_id, json_body).run()
        return updated_project._asdict()
