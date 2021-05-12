import os
# Redis.
REDIS_URL = os.getenv('REDIS_URL', 'redis://redis:6379/0')

# SQLAlchemy
SQLALCHEMY_DATABASE_URI = 'postgresql://postgres:postgres@db:5432/postgres'

STATIC_FOLDER = '../app/dist/star-tides/'

# Celery.
CELERY_CONFIG = {
    'broker_url': REDIS_URL,
    'result_backend': REDIS_URL,
    'include': [
        'star_tides.core.tasks.test_action.add_numbers'
    ]
}

CLIENT_ID = os.getenv('CLIENT_ID')