'''star_tides.services.databases.mongo.models.project_status
'''
from enum import Enum

class ProjectStatus(Enum):
    UNSPECIFIED = 'UNSPECIFIED'
    PROPOSED = 'PROPOSED'
    PROPOSED__HELP_WANTED = 'PROPOSED_HELP_WANTED'
    IN_PROGRESS = 'IN_PROGRESS'
    IN_PROGRESS_HELP_WANTED = 'IN_PROGRESS_HELP_WANTED'
    ABANDONED = 'ABANDONED'
    COMPLETED = 'COMPLETED'
