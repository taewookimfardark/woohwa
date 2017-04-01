from application import db
from application.helper.jwt.jwt_helper import (jwt_encode)

class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    email = db.Column(db.String(200))
    password = db.Column(db.String(500))
    name = db.Column(db.String(300))
    nick_name = db.Column(db.String(300))
    profile_image = db.Column(db.String(1024))
    profile_image_id = db.Column(db.Integer)
    gender = db.Column(db.Enum('MALE', 'FEMALE'), default='MALE')
    def get_token_string(self):
        data = {
            "email" : self.email,
            "id" : self.id
        }
        return jwt_encode(data)