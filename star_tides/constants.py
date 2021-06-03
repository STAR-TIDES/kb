''' star_tides.constants

This module contains constants to be used throughout the star_tides application.

'''

import string

# All ascii letters (not special chars) and numbers 0-9 for generating
# random strings
ALPHABET = string.ascii_letters + string.digits


class UserTypes:
    ''' Basic enum containing the types of authenticated users.
    '''
    COLLABORATOR=0
    ADMIN=1
    ALL=[COLLABORATOR, ADMIN]
