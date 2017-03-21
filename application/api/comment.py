from . import api
from application import db

from flask import request, jsonify
from application.helper.rest.request_query_helper import (
    model_to_dict, model_to_dict_params
)
from application.helper.rest.auth_helpler import (
    required_token, get_user_data_from_request
)

from application.models.user import User
from application.models.comment import Comment

@api.route('/comments', methods=['GET'])
@required_token
def get_comments():
    bucket_id = request.args['bucketId']

    if bucket_id is None:
        return jsonify(
            user_message="no bucket id"
        ), 400

    q = db.session.query(Comment, User).filter(Comment.bucket_id == bucket_id).join(User).join()

    q_list = q.all()
    data = []
    for (comment, user) in q_list:
        comment_dict = model_to_dict(comment)
        user_dict = model_to_dict_params(user, 'id', 'name', 'profileImage', 'profileImageId')
        comment_dict['user'] = user_dict
        data.append(comment_dict)

    return jsonify(
        data=data
    )

@api.route('/comments', methods=['POST'])
@required_token
def post_comments():
    request_params = request.get_json()

    message = request_params.get('message')
    bucket_id = request_params.get('bucketId')
    user_id = get_user_data_from_request(request)['id']

    print message
    print bucket_id
    print user_id

    if message is None or bucket_id is None or user_id is None:
        return jsonify(
            userMessage="invalid params"
        ), 400

    print 'gogo'

    comment = Comment(user_id=user_id,
                      bucket_id=bucket_id,
                      message=message)
    db.session.add(comment)
    db.session.commit()

    comment_dict = model_to_dict(comment)

    user = User.query.get(user_id)
    user_dict = model_to_dict_params(user, 'id', 'name', 'profileImage', 'profileImageId')

    comment_dict['user'] = user_dict

    return jsonify(
        data=comment_dict
    )
