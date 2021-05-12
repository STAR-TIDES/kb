from star_tides.create_app import celery_app as celery


@celery.task()
def another_task(one, two):
    return one + two
