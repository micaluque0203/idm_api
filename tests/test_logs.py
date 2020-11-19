from tests import db, app
from app.models.logs import Logs
from app.models.users import Users
from tests.fixtures.data.user_data_1 import USER_1, USER_2, USER_3, USER_4
import unittest
import json


class LogsTest(unittest.TestCase):
    def setUp(self):
        self.app = app
        self.app.config['TESTING'] = True
        self.app.config['DEBUG'] = False
        self.app.config['WTF_CSRF_ENABLED'] = False
        self.app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite://'
        self.app_context = self.app.app_context()
        with self.app_context:
            db.create_all()
        self.app_context.push()
        self.client = self.app.test_client(use_cookies=True)

    def tearDown(self):
        db.session.remove()
        db.drop_all()

    def test_logs_from_US_return_avg_of_requests(self):
        self.__create_log(USER_1)
        self.__create_log(USER_2)
        self.__create_log(USER_3)
        response = self.client.get("/logs/requests/US/avg")
        print(response.json)
        self.assertTrue(response.status_code == 200)
        self.assertTrue(response.json == {'avg': '1.5'})

    def test_user_distance_return_max_from_AR(self):
        self.__create_log(USER_1)
        self.__create_log(USER_2)
        response = self.client.get("/logs/distance/max")
        print(response.json)
        self.assertTrue(response.status_code == 200)
        self.assertTrue(response.json == {'max': 10000})

    def test_user_equal_distance_distinc_count_of_requests_return_max_from_AR(self):
        self.__create_log(USER_3)
        self.__create_log(USER_4)
        response = self.client.get("/logs/distance/max")
        print(response.json)
        self.assertTrue(response.status_code == 200)
        self.assertTrue(response.json == {'max': 10000})

    def test_user_distance_return_min_from_AR(self):
        self.__create_log(USER_1)
        self.__create_log(USER_2)
        response = self.client.get("/logs/distance/min")
        print(response.json)
        self.assertTrue(response.status_code == 200)
        self.assertTrue(response.json == {'min': 8949})


        #La IP 3.3.3.3 de España con 50 invocaciones (Se queda con la IP con
#más invocaciones si empatan la distancia)


    def __create_log(self, data):
        self.__add_user(data)
        self.__add_log(data)

    def __add_user(self, data):
        user = Users(data=data)
        db.session.add(user)
        db.session.commit()

    def __add_log(self, data):
        log = Logs(data=data)
        db.session.add(log)
        db.session.commit()