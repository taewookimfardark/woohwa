from application import db
from .model import TimestampMixin

class Comment(db.Model, TimestampMixin):
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