from application import db
from user import User

class Group(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(200))
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'))
    user = db.relationship(
        'User',
        foreign_keys=[user_id],
        backref=db.backref(
            'user_by_group',
            cascade='all, delete-orphan',
            lazy='dynamic'
        )
    )
    profile_image = db.Column(db.String(1024))
    profile_image_id = db.Column(db.Integer)
    description = db.Column(db.String(1000))
    created_time = db.Column(db.DateTime, default=db.func.now())
