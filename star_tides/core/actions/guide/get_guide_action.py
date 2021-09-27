'''star_tides.core.actions.guide.get_guide_action
'''
from mongoengine.errors import DoesNotExist
from star_tides.exceptions import NotFoundError
from star_tides.core.actions.base_action import Action
from star_tides.services.databases.mongo.models.guide_model import Guide
from star_tides.services.databases.mongo.schemas.guide_schema import GuideSchema


class GetGuideAction(Action):
    '''Action that gets a Guide document in the DB given a ProjectData.'''

    def __init__(self, guide_id):
        self.guide_id = guide_id

    def run(self) -> dict:
        try:
            guide = Guide.objects.get(id=self.guide_id)
        except DoesNotExist as e:
            raise NotFoundError(
                f'Could not find guide with ID {self.guide_id}.') from e
        return GuideSchema().dump(guide)

