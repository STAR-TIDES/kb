'''star_tides.core.data.engagement_data
'''

from typing import List, NamedTuple
from star_tides.core.data.location_data import LocationData

class EngagementData(NamedTuple):
    locations: List[LocationData]
    backgrounds: List[str]
    areas_of_interest: List[str]
    focuses: List[str]
