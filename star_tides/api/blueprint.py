from flask import Blueprint
from star_tides.services.sql.database.models.UserModel import UserModel
from star_tides.services.mongo.models.UserModel import User

bp = Blueprint('bp', __name__)


@bp.route('/foo')
def index():

    from star_tides.core.tasks.test_action import add_numbers
    from star_tides.core.tasks.second_test_action import another_task

    user = UserModel(
        first_name="Evan",
        last_name="K",
        email="foo@barbas.com"
    )
    #
    # mdb_user = User(first_name="Foobar", last_name="Shabam", email="shmoili@tabouli.com")
    # mdb_user.save()
    # db.session.add(user)
    # db.session.commit()
    #
    # result = another_task.delay(10, 10)
    # other_result = add_numbers.delay(10, 15)
    #
    # return str(f"Postgres user: {user.id}\nMongo User: {mdb_user.email}.\nYour task id is {result.task_id}\n{other_result.task_id}")
    return "It's an app yo"