'''Enums and utilities related to Contact Availability at the database-level.'''

from enum import Enum, auto

class Availability(Enum):
    '''Availability is an enum describing a Contact's availability.'''

    UNSPECIFIED = auto()
    UNAVAILABLE = auto()
    AVAILABLE = auto()
    