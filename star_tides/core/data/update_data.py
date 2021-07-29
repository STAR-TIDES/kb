'''star_tides.core.data.update_data
'''

from typing import NamedTuple, Optional, Text
import datetime


class UpdateData(NamedTuple):
    timestamp: datetime.datetime
    user_id: str
    content: str
    requesting_contact_id: Optional[Text] = None
