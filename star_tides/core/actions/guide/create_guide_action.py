'''star_tides.core.actions.guide.create_guide_action
'''

from marshmallow.exceptions import ValidationError
from star_tides.core.actions.base_action import Action
from star_tides.exceptions import InvalidParamError

from star_tides.services.databases.mongo.schemas.guide_schema import GuideSchema


class CreateGuideAction(Action):
    '''Action that creates a Guide document in the DB given a ProjectData.'''

    def __init__(self, json_body) -> None:
        self.body = json_body

    def run(self) -> dict:
        try:
            schema = GuideSchema().load(self.body)
        except ValidationError as e:
            raise InvalidParamError(
                f'Failed to validate using schema: {e.messages}') from e
        return GuideSchema(many=False).dump(schema)
