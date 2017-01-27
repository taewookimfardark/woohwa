from application import db

class RelationUserGroup(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'))
    user = db.relationship(
        'User',
        foreign_keys=[user_id],
        backref=db.backref(
            'groups_by_user',
            cascade='all, delete-orphan',
            lazy='dynamic')
        )
    group_id = db.Column(db.Integer, db.ForeignKey('group.id'))
    group = db.relatinoship(
        'Group',
        foreign_keys=[group_id],
        backref=db.backref(
            'users_by_group',
            cascade='all, delete-orphan',
            lazy='dynamic'
        )
    )
    edited_time = db.Column(
        db.DateTime,
        default=db.func.now(),
        onupdate=db.func.now())

    __table_args__ = (
        db.UniqueConstraint(
            'user_id',
            'group_id',
            name='unq_uid_gid'
        )
    )