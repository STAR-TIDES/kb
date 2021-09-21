''' star_tides.constants

This module contains constants to be used throughout the star_tides application.

'''

import enum
import string

# All ascii letters (not special chars) and numbers 0-9 for generating
# random strings
ALPHABET = string.ascii_letters + string.digits


class UserTypes(enum.Enum):
    ''' Basic enum containing the types of authenticated users.
    '''
    UNSPECIFIED = 0
    COLLABORATOR = 1
    ADMIN = 2
