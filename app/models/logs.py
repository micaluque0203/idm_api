from app.helpers.mysql import db


class Logs(db.Model):
    __tablename__ = 'logs'
    id = db.Column(db.Integer, primary_key=True)
    user_id = db.Column(db.Integer)
    ip = db.Column(db.String(100))
    timestamp = db.Column(db.DateTime())

    def __init__(self, data):
        self.user_id = data.get('user_id')
        self.ip = data.get('ip')
        self.timestamp = data.get('timestamp')
