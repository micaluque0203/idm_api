from tests import db, app
from app.models.logs import Logs
from app.models.users import Users
from freezegun import freeze_time
from app.adapters.aws import AwsRequest
from app.adapters.country import CountryRequest
from tests.fixtures.mocks.mock_1 import AWS_IP_PREFIX, COUNTRY_INFO, COUNTRY_API
from tests.fixtures.data.user_data import USER_1, USER_2, USER_3, USER_4
from unittest.mock import patch
import unittest
import json


class ApiTest(unittest.TestCase):

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

    @patch.object(AwsRequest, "get_ip_prefixs", return_value=AWS_IP_PREFIX)
    @patch.object(CountryRequest, "get_info", return_value=COUNTRY_API)
    @patch.object(CountryRequest, "get_country_by_ip", return_value=COUNTRY_INFO)
    @freeze_time("2020-11-17 03:05:12")
    def test_create_user_return_data(self, info_country, data_ip, is_aws_ip):
        data = self.__read_lead(lead_name=1)
        headers = {'user_id': '11233'}
        response = self.client.post("/users", json=data, headers=headers)
        expected_response = self.__read_response(response_name=1)
        self.assertTrue(info_country.called)
        self.assertTrue(data_ip.called)
        self.assertTrue(is_aws_ip.called)
        self.assertTrue(response.status_code == 200)
        self.assertTrue(response.json == expected_response)

    def __read_lead(self, lead_name):
        filename = 'tests/fixtures/leads/user_{lead_name}.json'.format(lead_name=lead_name)
        with open(filename, 'r') as lead_data:
            return json.load(lead_data)

    def __read_response(self, response_name):
        filename = 'tests/fixtures/responses/response_{response_name}.json'.format(response_name=response_name)
        with open(filename, 'r') as lead_data:
            return json.load(lead_data)

    def test_logs_from_US_return_avg_of_requests(self):
        self.__create_log(USER_1)
        self.__create_log(USER_2)
        self.__create_log(USER_3)
        response = self.client.get("/logs/requests/US/avg")
        self.assertTrue(response.status_code == 200)
        self.assertTrue(response.json == {'avg': 1.5})

    def test_user_distance_return_max_from_AR(self):
        self.__create_log(USER_1)
        self.__create_log(USER_2)
        response = self.client.get("/users/distance/max")
        self.assertTrue(response.status_code == 200)
        self.assertTrue(response.json == {'max': 10000})

    def test_user_distance_return_min_from_AR(self):
        self.__create_log(USER_1)
        self.__create_log(USER_2)
        response = self.client.get("/users/distance/min")
        self.assertTrue(response.status_code == 200)
        self.assertTrue(response.json == {'min': 8949})

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
