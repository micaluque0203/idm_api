from app.helpers.mysql import db, MySQLhandler
from app.helpers.utils import read_file
from app.models.users import Users
from sqlalchemy import desc, asc, func
from app.settings import QUERY_PATH


class IDMdata():

    def get_max_distance(self):
        mysql = MySQLhandler()
        query_path = QUERY_PATH + 'max.sql'
        query = read_file(query_path)
        data = mysql.get_data_by_query(query)
        return data.distance

    def get_min_distance(self):
        mysql = MySQLhandler()
        query_path = QUERY_PATH + 'min.sql'
        query = read_file(query_path)
        data = mysql.get_data_by_query(query)
        return data.distance

    def requests_avg_data(self, iso_code):
        mysql = MySQLhandler()
        query_path = QUERY_PATH + 'avg.sql'
        query = read_file(query_path, iso_code)
        data = mysql.get_data_by_query(query)
        return data[0]
