from application import db
from application.lib.jwt.jwt_helper import (jwt_encode)
from user import User

class UncompleteBucket(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    userid = db.Column(db.Integer, db.ForeignKey('user.id'))
    user = db.relationship(
        'User', foreign_keys=[userid],
        backref=db.backref(
            'uncomplete_bucket_list',
            cascade='all, delete-orphan',
            lazy='dynamic'
        )
    )
    title = db.Column(db.String((200)))
    when_month = db.Column(db.Integer)
    where = db.Column(db.String(200))
    info = db.Column(db.String(500))
    reward = db.Column(db.String(200))
    status = db.Column(db.Integer)
    iscomplete = db.Column(db.Boolean, default = False)
    excesslimit = db.Column(db.Boolean, default = False)

class CompleteBucket(db.Model):
    id = db.Column(db.Integer, primary_key = True)
    bucketid = db.Column(db.Integer, db.ForeignKey('uncomplete_bucket.id'))
    uncomplete_bucket = db.relationship(
        'UncompleteBucket', foreign_keys=[bucketid],
        backref=db.backref(
            'complete_bucket_list',
            cascade='all, delete-orphan',
            lazy='dynamic'
        )
    )
    completedate = db.Column(db.String(200))
    completecomment = db.Column(db.String(500))

