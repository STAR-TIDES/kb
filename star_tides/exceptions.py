''' star_tides.exceptions.base_exception
'''

# pragma pylint: disable=E1124

from http import HTTPStatus


# LOG LEVELS
SEVERITY_DEBUG = 'DEBUG'
SEVERITY_INFO = 'INFO'
SEVERITY_WARNING = 'WARNING'
SEVERITY_ERROR = 'ERROR'
SEVERITY_CRITICAL = 'CRITICAL'


class StarTidesException(Exception):
    ''' Base exception for all of exceptions.

        Args:
            error_code -  internal error code for logging, hard-coded in error
                          class
            response_msg - error msg returned to client, hard-coded in error
                           class
            logging_msg - error msg logged in <name of project here>
            severity - log level
            http_code - error code returned to client
    '''
    def __init__(
        self,
        error_class: str,
        response_msg: str,
        severity: str,
        logging_msg: str = None,
        http_code: int = HTTPStatus.OK
    ):
        super().__init__()
        self.error_class = error_class
        self.response_msg = response_msg
        self.severity = severity
        self.http_code = http_code

        if logging_msg is None:
            self.logging_msg = response_msg


# Api errors - 1000s
class InvalidParamError(StarTidesException):
    def __init__(self,
                 response_msg='Invalid parameters received',
                 logging_msg=None,
                 severity=SEVERITY_ERROR, http_code=HTTPStatus.BAD_REQUEST
    ):
        super().__init__(
            self.__class__.__name__, response_msg, severity,
            http_code, logging_msg=logging_msg
        )

# Database Errors


class RecordDoesNotExistError(StarTidesException):
    def __init__(self,
                 response_msg='Record does not exist in database',
                 logging_msg=None,
                 severity=SEVERITY_ERROR, http_code=HTTPStatus.NOT_FOUND
    ):
        super().__init__(
            self.__class__.__name__, response_msg, severity,
            http_code, logging_msg=logging_msg
        )

# Action Error


class ActionError(StarTidesException):
    def __init__(self,
                 response_msg='A generic Action error occurred',
                 logging_msg=None,
                 severity=SEVERITY_ERROR,
                 http_code=HTTPStatus.INTERNAL_SERVER_ERROR
    ):
        super().__init__(
            self.__class__name__, response_msg, severity,
            http_code, logging_msg=None
        )


# Auth Errors


class AuthenticationError(StarTidesException):
    def __init__(self,
                 response_msg='Failed to authenticate',
                 logging_msg=None,
                 severity=SEVERITY_ERROR,
                 http_code=HTTPStatus.UNAUTHORIZED
    ):
        super().__init__(
            self.__class__name__, response_msg, severity,
            http_code, logging_msg=logging_msg
        )
