import unittest
from app import app
from app.helpers.mysql import db
from tests.test_users import UsersTest
from tests.test_logs import LogsTest


class Init(unittest.TestCase):

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

    def test_404(self):
        response = self.client.get('/wrong/url')
        self.assertTrue(response.status_code == 404)

    def test_hi_200(self):
        response = self.client.get('/')
        self.assertTrue(response.status_code == 200)


Init()
UsersTest()
LogsTest()
if __name__ == "__main__":
    unittest.main(warnings='ignore')
