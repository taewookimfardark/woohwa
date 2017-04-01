from . import api
from application import db

from flask import request, jsonify
from application.helper.rest.request_query_helper import (
    model_to_dict, model_to_dict_params, to_snakecase
)

from application.helper.rest.auth_helpler import (
    required_token, get_user_data_from_request
)

from application.models.group import Group
from application.models.relation_user_group import RelationUserGroup
from application.models.user import User

@api.route('/relation-user-groups', methods=['POST'])
@required_token
def post_relation_user_group():
    request_params = request.get_json()
    user_id = request_params.get('userId')
    group_id = request_params.get('groupId')
    status = request_params.get('status')
    relation_user_group = RelationUserGroup(user_id=user_id, group_id=group_id, status=status)
    db.session.add(relation_user_group)
    db.session.commit()
    relation_user_group_dict = model_to_dict(relation_user_group)
    print relation_user_group_dict
    user = User.query.get(user_id)
    group = Group.query.get(group_id)
    relation_user_group_dict['user'] = model_to_dict_params(user, 'id', 'email', 'name', 'profileImage', 'profileImageId')
    relation_user_group_dict['group'] = model_to_dict(group)

    return jsonify(
        data=relation_user_group_dict
    )

@api.route('/relation-user-groups', methods=['GET'])
@required_token
def get_relation_user_group():
    user_id = get_user_data_from_request(request)['id']
    group_id = request.args.get('groupId')

    q = db.session.query(RelationUserGroup, Group, User)

    if group_id is not None:
        q = q.filter(RelationUserGroup.group_id == group_id)
    else:
        q = q.filter(RelationUserGroup.user_id == user_id)

    q = q.join(Group, Group.id == RelationUserGroup.id).join(User, User.id == RelationUserGroup.user_id).join()


    q_result = q.all()

    data = []
    for (relation_user_group, group, user) in q_result:
        relation_user_group_dict = model_to_dict(relation_user_group)
        group_dict = model_to_dict(group)
        relation_user_group_dict['group'] = group_dict
        relation_user_group_dict['user'] = model_to_dict_params(user, 'id', 'email', 'name', 'profileImage', 'profileImageId')
        data.append(relation_user_group_dict)


    return jsonify(
        data=data
    )

@api.route('/members/<int:group_id>', methods=['GET'])
@required_token
def get_group_members(group_id):
    q = db.session.query(RelationUserGroup, User).filter(RelationUserGroup.group_id == group_id) \
        .join(User, RelationUserGroup.user_id == User.id)
    q_result = q.all()

    data = []
    for (relation_user_group, user) in q_result:
        user_dict = model_to_dict_params(user, 'id', 'email', 'name', 'profileImage', 'profileImageId')
        data.append(user_dict)

    return jsonify(
        data=data
    )
