from . import api
from application import db

import datetime
from flask import request, jsonify
from application.helper.rest.request_query_helper import (
    model_to_dict, model_to_dict_params, to_snakecase
)

from application.helper.rest.auth_helpler import (
    required_token, get_user_data_from_request
)

from application.models.bucket import Bucket
from application.models.user import User

@api.route('/buckets', methods=['POST'])
@required_token
def post_buckets():
    request_params = request.get_json()

    user_id = get_user_data_from_request(request)['id']
    group_id = request_params.get('groupId')
    description = request_params.get('description')
    title = request_params.get('title')
    profile_image = request_params.get('profileImage')
    profile_image_id = request_params.get('profileImageId')

    bucket = Bucket(group_id=group_id,
                    user_id=user_id,
                    description=description,
                    title=title,
                    profile_image=profile_image,
                    profile_image_id=profile_image_id)

    db.session.add(bucket)
    db.session.commit()

    bucket_dict = model_to_dict(bucket)
    user = User.query.get(user_id)
    user_dict = model_to_dict_params(user, 'id', 'name', 'profileImage', 'profileImageId')
    bucket_dict['user'] = user_dict

    return jsonify(
        data=bucket_dict
    )

@api.route('/buckets', methods=['GET'])
@required_token
def get_buckets():
    group_id = request.args['groupId']

    if group_id is None:
        return jsonify(
            user_mseeage="no group id"
        ), 400

    q = Bucket.get_base_query()

    query_list = q.all()

    data = []

    for (bucket, user, complete_user) in query_list:
        bucket_dict = model_to_dict(bucket)
        if user is not None:
            user_dict = model_to_dict_params(user, 'id', 'name', 'profileImage', 'profileImageId')
            bucket_dict['user'] = user_dict
        if complete_user is not None:
            complete_user_dict = model_to_dict_params(complete_user, 'id', 'name', 'profileImage', 'profileImageId')
            bucket_dict['complete_user'] = complete_user_dict
        data.append(bucket_dict)

    return jsonify(
        data=data
    )

@api.route('/buckets/<int:bucket_id>', methods=['PUT'])
@required_token
def put_buckets(bucket_id):
    request_params = request.get_json()
    bucket = Bucket.query.get(bucket_id)

    if bucket is None:
        return jsonify(
            userMessage='no bucket'
        ), 400

    for param in request_params:
        col = to_snakecase(param)
        val = request_params.get(param)
        if col == 'complete_date':
            val = datetime.datetime.fromtimestamp(val)
        setattr(bucket, col, val)
    db.session.commit()

    return jsonify(
        data=model_to_dict(bucket)
    )
