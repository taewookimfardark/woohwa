from application import db
from bucket import Bucket
from user import User

class Comment(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'))
    user = db.relationship(
        'User',
        foreign_keys=[user_id],
        backref=db.backref(
            'user_by_comment',
            cascade='all, delete-orphan',
            lazy='dynamic'
        )
    )
    bucket_id = db.Column(db.Integer, db.ForeignKey('bucket.id'))
    bucket = db.relationship(
        'Bucket',
        foreign_keys=[bucket_id],
        backref=db.backref(
            'bucket_by_comment',
            cascade='all, delete-orphan',
            lazy='dynamic'
        )
    )
    message = db.Column(db.String(1024))
    created_time = db.Column(db.DateTime, default=db.func.now())
    edited_time = db.Column(db.DateTime, default=db.func.now(), onupdate=db.func.now())