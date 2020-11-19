from os import environ

APP_NAME = environ.get('APP_NAME', 'idm')
APP_VERSION = environ.get('VERSION', 'V1')
APP_HOST = environ.get('APP_PORT', 'localhost')
APP_PORT = int(environ.get('APP_PORT', 8009))
ENVIRONMENT = environ.get('ENVIRONMENT')
DEBUG = environ.get('DEBUG', 'False')
MYSQL_HOST = environ.get('MYSQL_HOST')
MYSQL_USER = environ.get('MYSQL_USER')
MYSQL_PSWD = environ.get('MYSQL_PSWD')
MYSQL_DATABASE = environ.get('MYSQL_DATABASE')
MYSQL_PORT = environ.get('MYSQL_PORT')
API_COUNTRY_IP = environ.get('API_COUNTRY_IP')
API_AWS_IP = environ.get('API_AWS_IP')
API_COUNTRY_INFO = environ.get('API_COUNTRY_INFO')
DATABASE_URL = environ.get('DATABASE_URL')
QUERY_PATH = './migrations/querys/'
