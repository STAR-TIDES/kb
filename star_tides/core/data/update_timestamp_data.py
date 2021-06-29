'''star_tides.core.data.update_timestamp_data
'''
from typing import NamedTuple
import datetime


class UpdateTimestampData(NamedTuple):
    timestamp: datetime.datetime
    user_id: str
