'''star_tides.core.actions.guide.list_guide_action
'''

from star_tides.core.actions.base_action import Action
from star_tides.exceptions import InvalidParamError

from star_tides.services.databases.mongo.models.guide_model import Guide
from star_tides.services.databases.mongo.schemas.guide_schema import GuideSchema


class ListGuidesAction(Action):
    '''Action that creates a Guide document in the DB given a ProjectData.'''

    def __init__(self, limit: int = 50, offset: int = 0) -> None:
        self.limit = limit
        self.offset = offset

    @property
    def limit(self):
        return self._limit

    @limit.setter
    def limit(self, val):
        if isinstance(val, str):
            if val.isdigit():
                val = int(val)
                if val < 1:
                    raise InvalidParamError('Limit must be greater than 0.')
                self._limit = val
            else:
                raise InvalidParamError('Limit must be an integer greater '
                                        'than 0.')
        else:
            raise InvalidParamError('Invalid parameter type.')

    @property
    def offset(self):
        return self._offset

    @offset.setter
    def offset(self, val):
        if isinstance(val, str):
            if val.isdigit():
                val = int(val)
                if val < 0 or val > 100:
                    raise InvalidParamError('Offset must be 0 or greater, '
                                            'and less than 100.')
                self._offset = val
            else:
                raise InvalidParamError('Limit must be an integer greater than '
                                    '0 and less than 100.')
        else:
            raise InvalidParamError('Invalid parameter type.')

    def run(self) -> dict:
        guides = Guide.objects.skip(self.offset).limit(self.limit)
        data = GuideSchema(many=True).dump(guides)
        return {
            'limit': self.limit,
            'offset': self.offset,
            'length': len(data),
            'data': data
        }

