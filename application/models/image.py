from application import db

class Image(db.Model):
    id = db.Column(db.Integer, parimary_key=True)
    storage_key = db.Column(db.String(255))
    serving_url = db.Column(db.String(1024))
    uploader_id = db.Column(db.Integer, db.ForeignKey('user.id'))
