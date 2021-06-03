''' star_tides.services.interfaces.utils.logging_decorator
'''
from functools import wraps


def interface_decorator(func):
    ''' A decorator to give the same functionality as having a base class
    that handles logging the start of execution and the end of execution,
    but is more conducive to the interface design.

    A base class fails the interface because we do not have one class per
    business logic 'case', rather we have one interface per mongodb collection.
    It would be pretty ridiculous to have 4 different 'interface' modules when
    each method would contain such closely related content.
    '''
    @wraps(func)
    def wrapper(*args, **kwargs):
        # TODO: Implement pre and post execution logging
        return func(*args, **kwargs)
    return wrapper
