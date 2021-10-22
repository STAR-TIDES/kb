'''star_tides.core.actions.list_projects_action
'''
from star_tides.core.data.project_data import ProjectData
from star_tides.services.databases.mongo.models.project_model import ProjectModel
from star_tides.config.settings import DEFAULT_PAGE_SIZE
from star_tides.core.actions.base_action import Action


class ListProjectsAction(Action):
    def run(self):
        return [ProjectData.from_model(model) for model in
                ProjectModel.objects.order_by('name')[:DEFAULT_PAGE_SIZE]]
