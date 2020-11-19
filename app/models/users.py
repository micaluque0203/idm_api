from app.helpers.mysql import db


class Users(db.Model):
    __tablename__ = 'users'
    id = db.Column(db.Integer, primary_key=True)
    ip = db.Column(db.String(100))
    country = db.Column(db.String(100))
    distance = db.Column(db.Integer)
    iso_code = db.Column(db.String(100))
    timestamp = db.Column(db.DateTime())

    def __init__(self, data):
        self.ip = data.get('ip')
        self.country = data.get('country_name')
        self.distance = data.get('distance')
        self.iso_code = data.get('iso_code')
        self.timestamp = data.get('timestamp')
