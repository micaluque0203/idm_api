from app.helpers.mysql import db, MySQLhandler
from app.helpers.utils import read_file
from app.models.users import Users
from sqlalchemy import desc, asc, func
from app.settings import QUERY_PATH


class Logs():

    def get_max_distance(self):
        mysql = MySQLhandler()
        query_path = QUERY_PATH + 'max.sql'
        query = read_file(query_path)
        data = mysql.get_data_by_query(query)
        print("BATMAN", data)
        return data

    def get_min_distance(self):
        data = (db.session.query(Users).order_by(asc(Users.distance)).first())
        return data.distance

    def requests_avg_data(self, iso_code):

        mysql = MySQLhandler()
        query = read_file(QUERY_PATH, iso_code)
        data = mysql.get_data_by_query(query)
        return data
