'''star_tides.core.actions.guide.update_guide_action
'''

from star_tides.core.actions.base_action import Action


class UpdateGuideAction(Action):
    '''Action that updates a Guide document in the DB given a ProjectData.'''

    def __init__(self, _id, json_body) -> None:
        self.guide_id = _id
        self.body = json_body


    def run(self):
        raise NotImplementedError()
    # def run(self) -> dict:
    #     try:
    #         schema = GuideUpdateSchema().load(
    #             self.body, partial=self.body.keys())
    #         print(f'Schema is: {schema}')
    #     except ValidationError as e:
    #         raise InvalidParamError(
    #             f'Failed to validate using schema: {e.messages}') from e
    #     return GuideUpdateSchema(many=False).dump(schema)
