from star_tides.create_app import celery_app as celery


@celery.task()
def add_numbers(one, two):
    return one + two
