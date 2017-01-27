from application import db

class Group(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(200))
    description = db.Column(db.String(1000))
    created_time = db.Column(db.DateTime, default=db.func.now(), onupdate=db.func.now())
