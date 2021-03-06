from application import db

class Image(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    serving_url = db.Column(db.String(1024))
    storage_url = db.Column(db.String(1024))
    uploader_id = db.Column(db.Integer, db.ForeignKey('user.id',
                                                      ondelete="set null"))