from flask_sqlalchemy import SQLAlchemy


db = SQLAlchemy()


class MySQLhandler():
    def get_data_by_query(self, query):
        data = db.engine.execute(query)
        result = []
        for row in data:
            result.append(row)
        print(data.first()[0])
        return data.first()[0]






