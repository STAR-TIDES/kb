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
        error_code: int,
        response_msg: str,
        logging_msg: str,
        severity: str,
        http_code: int = 400
    ):
        super().__init__()
        self.error_code = error_code
        self.response_msg = response_msg
        self.logging_msg = logging_msg
        self.severity = severity
        self.http_code = http_code


# Api errors - 1000s

class ParamInvalidError(StarTidesException):
    def __init__(self,
                 logging_msg='Invalid parameters received',
                 severity=SEVERITY_WARNING, http_code=HTTP_BAD_REQUEST_ERROR_400
    ):
        super().__init__(
            1000, 'Invalid parameters received', logging_msg, severity,
            http_code
        )
