''' star_tides.exceptions.base_exception
'''



# LOG LEVELS
SEVERITY_DEBUG = 'DEBUG'
SEVERITY_INFO = 'INFO'
SEVERITY_WARNING = 'WARNING'
SEVERITY_ERROR = 'ERROR'
SEVERITY_CRITICAL = 'CRITICAL'


# CLIENT RESPONSE CONSTANTS
HTTP_SUCCESS_200 = 'SUCCESS'
HTTP_RESOURCE_ERROR_404 = 'RESOURCE_ERROR'
HTTP_BAD_REQUEST_ERROR_400 = 'BAD_REQUEST_ERROR'
HTTP_UNAUTHORIZED_ERROR_401 = 'UNAUTHORIZED_ERROR'
HTTP_FORBIDDEN_ERROR_403 = 'FORBIDDEN_ERROR'
HTTP_SYSTEM_ERROR_500 = 'SYSTEM_ERROR'

RESPONSE_CONSTANTS_TO_INT = {
    'SUCCESS': 200,
    'RESOURCE_ERROR': 404,
    'BAD_REQUEST_ERROR': 400,
    'UNAUTHORIZED_ERROR': 401,
    'FORBIDDEN_ERROR': 403,
    'SYSTEM_ERROR': 500
}


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
        logging_msg: str,
        severity: str,
        http_code: int = 400
    ):
        super().__init__()
        self.error_class = error_class
        self.response_msg = response_msg
        self.logging_msg = logging_msg
        self.severity = severity
        self.http_code = http_code


# Api errors - 1000s
class ParamInvalidError(StarTidesException):
    def __init__(self,
                 response_msg='Invalid parameters received',
                 logging_msg='Invalid parameters received',
                 severity=SEVERITY_ERROR, http_code=HTTP_BAD_REQUEST_ERROR_400
    ):
        super().__init__(
            self.__class__.__name__, response_msg, logging_msg, severity,
            http_code
        )

# Database Errors


class RecordDoesNotExistError(StarTidesException):
    def __init__(self,
                 response_msg='Record does not exist in database',
                 logging_msg='Record does not exist in database',
                 severity=SEVERITY_ERROR, http_code=HTTP_BAD_REQUEST_ERROR_400
    ):
        super().__init__(
            self.__class__.__name__, response_msg, logging_msg, severity,
            http_code
        )

# Action Error


class GenericActionError(StarTidesException):
    def __init__(self,
                 response_msg='A generic Action error occurred',
                 logging_msg='A generic Action error occurred',
                 severity=SEVERITY_ERROR,
                 http_code=HTTP_BAD_REQUEST_ERROR_400
    ):
        super().__init__(
            self.__class__name__, response_msg, logging_msg, severity,
            http_code
        )


# Auth Errors


class AuthenticationFailureError(StarTidesException):
    def __init__(self,
                 response_msg='Failed to authenticate',
                 logging_msg='Failed to authenticate',
                 severity=SEVERITY_ERROR,
                 http_code=HTTP_UNAUTHORIZED_ERROR_401
    ):
        super().__init__(
            self.__class__name__, response_msg, logging_msg, severity,
            http_code
        )
