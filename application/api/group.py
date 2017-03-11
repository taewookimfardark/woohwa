from . import api
from application import db

from flask import request, jsonify
from application.helper.rest.request_query_helper import (
    model_to_dict
)

from application.helper.rest.auth_helpler import (
    required_token, get_user_data_from_request
)

from application.models.group import Group
from application.models.relation_user_group import RelationUserGroup
from application.models.bucket import Bucket

@api.route('/groups', methods=['POST'])
@required_token
def post_groups():
    request_params = request.get_json()
    name = request_params.get('name')
    description = request_params.get('description')
    profile_image = request_params.get('profileImage')
    profile_image_id = request_params.get('profileImageId')

    user_id = get_user_data_from_request(request)['id']
    group = Group(name=name, description=description, profile_image=profile_image, profile_image_id=profile_image_id, user_id=user_id)
    db.session.add(group)
    db.session.commit()

    relation_user_group = RelationUserGroup(user_id=user_id, group_id=group.id)
    db.session.add(relation_user_group)
    db.session.commit()

    return jsonify(
        data={
            'group': model_to_dict(group),
            'relation_user_group': model_to_dict(relation_user_group)
        }
    )

@api.route('/groups', methods=['GET'])
def get_groups():
    user_id = get_user_data_from_request(request).id

    q = db.session.query(RelationUserGroup).filter(RelationUserGroup.user_id == user_id)
    relation_user_groups = q.all()

    groups = []
    for relation in relation_user_groups:
        tmp_group = db.session.query(Group).filter(Group.id == relation.group_id)
        groups.append(model_to_dict(tmp_group))

    return jsonify(
        data=groups
    )

@api.route('/groups/<int:group_id>/buckets', methods=['GET'])
def get_group_buckets(group_id):

    q = db.session.query(Bucket).filter(Bucket.group_id == group_id)

    bucket_list = []
    buckets = q.all()

    for bucket in buckets:
        bucket_list.append(model_to_dict(bucket))

    return jsonify(
        data=bucket_list
    )


