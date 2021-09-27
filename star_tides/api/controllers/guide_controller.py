'''star_tides.api.controllers.guide_controller
'''

from star_tides.exceptions import InvalidParamError
from star_tides.api.controllers.base_controller import Controller
from star_tides.api.controllers import snake_case_dict
from star_tides.core.actions.guide.create_guide_action import CreateGuideAction
from star_tides.core.actions.guide.list_guide_action import ListGuidesAction
from star_tides.core.actions.guide.get_guide_action import GetGuideAction
from star_tides.core.actions.guide.delete_guide_action import DeleteGuideAction
from star_tides.core.actions.guide.update_guide_action import UpdateGuideAction


class ListGuidesController(Controller):
    def process_request(self) -> dict:
        args = Controller.get_query_params()
        params = {}
        if args.get('limit'):
            params['limit'] = args.get('limit')
        if args.get('offset'):
            params['offset'] = args.get('offset')
        guides = ListGuidesAction(**params).run()
        return guides


class GetGuideController(Controller):
    def __init__(self, guide_id: str) -> None:
        self.guide_id = guide_id

    def process_request(self) -> dict:
        guide = GetGuideAction(self.guide_id).run()
        return guide


class CreateGuideController(Controller):
    '''Creates a Guide in the DB given the JSON body in the request.'''

    def process_request(self) -> dict:
        body = self.get_request_body()
        if not body:
            raise InvalidParamError('Expected JSON body to be present.')
        json_body = snake_case_dict(body)
        # TODO(ljr): Pass to ContactSchema first?
        created_contact = CreateGuideAction(json_body).run()
        # return created_contact._asdict()
        return created_contact


class DeleteGuideController(Controller):
    def __init__(self, contact_id: str) -> None:
        self.contact_id = contact_id

    def process_request(self):
        response = DeleteGuideAction(self.contact_id).run()
        return response


class UpdateGuideController(Controller):
    def __init__(self, guide_id: str) -> None:
        self.guide_id = guide_id,

    def process_request(self):
        updated_guide = UpdateGuideAction(
            self.guide_id, self.get_request_body()).run()
        return updated_guide
