'''star_tides.api.route.project_route
'''

from star_tides.api.controllers.project_controller import CreateProjectController, DeleteProjectController, GetProjectController, ListProjectsController, UpdateProjectController
from star_tides.api.decorators.login_required import login_required
from flask.blueprints import Blueprint

project = Blueprint('project', __name__, url_prefix='/projects/')


@project.route('/', methods=['GET'])
def list_projects():
    return ListProjectsController().execute()


@project.route('/<project_id>', methods=['GET'])
def get_project(project_id: str):
    return GetProjectController(project_id).execute()


@project.route('/', methods=['POST'])
@login_required
def create_project():
    return CreateProjectController().execute()


@project.route('/<project_id>', methods=['DELETE'])
@login_required
def delete_project(project_id: str):
    return DeleteProjectController(project_id).execute()


@project.route('/<project_id>', methods=['PUT'])
@login_required
def update_project(project_id: str):
    return UpdateProjectController(project_id).execute()
