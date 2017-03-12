from application import db
from bucket_image import BucketImage

class Bucket(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    group_id = db.Column(db.Integer, db.ForeignKey('group.id'))
    group = db.relationship('Group', foreign_keys=[group_id])
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'))
    user = db.relationship('User', foreign_keys=[user_id])
    status = db.Column(db.Enum('REQUESTED', 'ACCEPTED', 'REJECTED', 'COMPLETED'), default='REQUESTED')
    title = db.Column(db.String(500))
    description = db.Column(db.String(1000))
    completed_time = db.Column(db.DateTime)
    profile_image = db.Column(db.String(1024))
    profile_image_id = db.Column(db.Integer)






