from application import db

class BucketImage(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    serving_url = db.Column(db.String(1024))
    storage_url = db.Column(db.String(1024))
    bucket_id = db.Column(db.Integer, db.ForeignKey('bucket.id'))
    bucket = db.relationship('Bucket', foreign_keys=[bucket_id])