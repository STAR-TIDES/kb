'''
star_tides.services.databases.mongo.models.availability

Enums and utilities related to Contact Availability at the database-level.
'''

from enum import Enum, unique
from typing import Any

from mongoengine.errors import ValidationError


@unique
class Availability(Enum):
    '''Availability is an enum describing a Contact's availability.'''

    # Use string values here so that they are appropriately encoded in our API.
    # I.e., we send these strings over the network instead of opaque ints.
    UNSPECIFIED = 'UNSPECIFIED'
    UNAVAILABLE = 'UNAVAILABLE'
    AVAILABLE = 'AVAILABLE'


def availability_validator(value: Any) -> None:
    if isinstance(value, int):
        try:
            _ = Availability(value)
            return
        except ValueError as error:
            raise ValidationError('not a valid Availability value') from error
    if isinstance(value, str):
        try:
            _ = Availability[value]
            return
        except ValueError as error:
            raise ValidationError('not a valid Availability name') from error
    raise ValidationError(
        f'cannot convert a {type(value)} into an Availabilty')
