from application import db

class Bucket(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    group_id = db.Column(db.Integer, db.foreignKey('group.id'))
    group = db.relationship('Group', foreign_keys=[group_id])
    user_id = db.Column(db.Integer, db.foreignKey('user.id'))
    user = db.relationship('User', foreign_keys=[user_id])
    description = db.Column(db.String(1000))
    complete_message = db.Column(db.String(1000))
    start_date = db.Column(db.dateTime, default=db.func.now())
    limit_date = db.Column(db.dateTime)
    end_date = db.Column(db.dateTime)
    profile_image_id = db.Column(db.Integer, db.foreignKey('image.id'))
    profile_image = db.relationship('Image', foreign_keys=[profile_image_id])





