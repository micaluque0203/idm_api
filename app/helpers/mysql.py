from flask_sqlalchemy import SQLAlchemy


db = SQLAlchemy()


class MySQLhandler():
    def get_data_by_query(self, query):
        data = db.engine.execute(query)
        for row in data:
            return row
