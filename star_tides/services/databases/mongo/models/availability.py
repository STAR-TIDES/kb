'''
star_tides.services.databases.mongo.models.availability

Enums and utilities related to Contact Availability at the database-level.
'''

from enum import Enum, unique
from typing import Any, Tuple

from mongoengine.errors import ValidationError


@unique
class Availability(Enum):
    '''Availability is an enum describing a Contact's availability.'''

    # Use string values here so that they are appropriately encoded in our API.
    # I.e., we send these strings over the network instead of opaque ints.
    UNSPECIFIED = 'UNSPECIFIED'
    UNAVAILABLE = 'UNAVAILABLE'
    AVAILABLE = 'AVAILABLE'

    def describe(self) -> Tuple[str, int]:
        return self.name, self.value

    def __str__(self) -> str:
        return str(self.name)


def availability_validator(value: Any) -> None:
    tups = {a.describe() for a in Availability}
    for t in tups:
        if value in t:
            return
    raise ValidationError(
        f'cannot convert {value} of type {type(value)} into an Availability')
