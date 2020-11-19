from flask import Flask
from app.helpers.mysql import db
from flask_script import Manager
from flask_migrate import Migrate, MigrateCommand
from app.settings import DEBUG, DATABASE_URL

app = Flask(__name__)
app.secret_key = None
app.debug = DEBUG
app.config['SQLALCHEMY_DATABASE_URI'] = DATABASE_URL
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
migrate = Migrate(app, db)
manager = Manager(app)

db.init_app(app)
manager.add_command('db', MigrateCommand)

from . import views
