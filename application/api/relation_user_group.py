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

@api.route('/relation_user_groups', methods=['POST'])
@required_token
def post_relation_user_group():
    request_params = request.get_json()
    user_id = request_params.get('user_id')
    group_id = request_params.get('group_id')
    relation_user_group = RelationUserGroup(user_id=user_id, group_id=group_id)
    db.session.add(relation_user_group)
    db.session.commit()

    return jsonify(
        data=relation_user_group
    )

@api.route('/relation_user_groups', methods=['GET'])
@required_token
def get_relation_user_group():
    user_id = get_user_data_from_request(request)['id']

    q = db.session.query(RelationUserGroup, Group).filter(RelationUserGroup.user_id == user_id) \
        .join(Group, Group.id == RelationUserGroup.group_id) \
        .join()

    q_result = q.all()

    data = []
    for (relation_user_group, group) in q_result:
        relation_user_group_dict = model_to_dict(relation_user_group)
        group_dict = model_to_dict(group)
        relation_user_group_dict['group'] = group_dict
        data.append(relation_user_group_dict)


    return jsonify(
        data=data
    )