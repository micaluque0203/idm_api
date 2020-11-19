from app.models.users import Users
from app.models.logs import Logs
from app.helpers.mysql import db


class IngestService():
    def ingest_user(self, user_data):
        try:
            user = Users(data=user_data)
            db.session.add(user)
            db.session.commit()
        except BaseException as err:
            msg = {
                'error': 'MYSQL_ERROR',
                'msw': err,
            }
            raise BaseException(msg)

    def ingest_log(self, log_data):
        try:
            new_log = Logs(data=log_data)
            db.session.add(new_log)
            db.session.commit()
        except BaseException as err:
            msg = {
                'error': 'MYSQL_ERROR',
                'msw': err,
            }
            raise BaseException(msg)
