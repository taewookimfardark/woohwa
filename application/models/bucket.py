from application import db
from user import User
from .model import TimestampMixin

class Bucket(db.Model, TimestampMixin):
    id = db.Column(db.Integer, primary_key=True)
    group_id = db.Column(db.Integer, db.ForeignKey('group.id'))
    group = db.relationship('Group', foreign_keys=[group_id])
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'))
    status = db.Column(db.Enum('REQUESTED', 'ACCEPTED', 'REJECTED', 'COMPLETED'), default='REQUESTED')
    title = db.Column(db.String(500))
    description = db.Column(db.String(1000))
    complete_message = db.Column(db.String(500))
    complete_message_user_id = db.Column(db.Integer, db.ForeignKey('user.id'))
    complete_date = db.Column(db.TIMESTAMP)
    profile_image = db.Column(db.String(1024))
    profile_image_id = db.Column(db.Integer)

    @classmethod
    def get_base_query(cls,
                       limit=None):
        user = db.aliased(User)
        complete_user = db.aliased(User)
        q = db.session.query(Bucket, user, complete_user) \
            .outerjoin(user, Bucket.user_id == user.id) \
            .outerjoin(complete_user, Bucket.complete_message_user_id == complete_user.id)

        if limit:
            q = q.limit(limit)

        return q






