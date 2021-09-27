'''star_tides.core.actions.guide.update_guide_action
'''

from marshmallow.exceptions import ValidationError
from star_tides.core.actions.base_action import Action
from star_tides.exceptions import InvalidParamError

from star_tides.services.databases.mongo.schemas.guide_schema import (
    GuideUpdateSchema
)


class UpdateGuideAction(Action):
    '''Action that updates a Guide document in the DB given a ProjectData.'''

    def __init__(self, id, json_body) -> None:
        self.guide_id = id
        self.body = json_body

    def run(self) -> dict:
        try:
            schema = GuideUpdateSchema().load(self.body, partial=self.body.keys())
            print(f'Schema is: {schema}')
        except ValidationError as e:
            raise InvalidParamError(
                f'Failed to validate using schema: {e.messages}') from e
        return GuideUpdateSchema(many=False).dump(schema)
