from . import api
from application import db
from application.models.user import User

from flask import request, jsonify
from application.helper.rest.request_query_helper import (
    model_to_dict, model_to_dict_params
)
from application.helper.rest.auth_helpler import (
    required_token, get_user_data_from_request
)

from sqlalchemy import and_
from sqlalchemy import or_


#from application.lib.storage.cloud_storage_helper import upload_image

import json
import sys
reload(sys)
sys.setdefaultencoding('utf-8')


@api.route("/")
def heool():
    return "hello woohwa"

@api.route('/login', methods=['POST'])
def login():
    request_params = request.get_json()

    email = request_params.get('email')
    password = request_params.get('password')

    user = db.session.query(User).filter(and_(User.email == email, User.password == password)).first()

    if user is None:
        return jsonify(
            userMessage = "no user"
        ), 400

    data = model_to_dict(user)
    token = user.get_token_string()

    return jsonify(
        data = data,
        token = token
    )



@api.route("/users", methods=['GET'])
def get_users():
    users = User.query.all()
    query_list = []
    for user in users:
        temp = model_to_dict_params(user, 'id', 'name', 'email', 'profileImage', 'profileImageId')
        query_list.append(temp)

    return jsonify(
        data = query_list
    )

@api.route('/users', methods=['POST'])
def post_users():
    request_params = request.get_json()
    email = request_params.get('email')
    password = request_params.get('password')
    name = request_params.get('name')
    gender = request_params.get('gender')
    profile_image = request_params.get('profileImage')
    profile_image_id = request_params.get('profileImageId')

    q = db.session.query(User).filter(User.email == email)

    if q.count() > 0 :
        return jsonify(
            userMessage = "enrolled email"
        ), 400

    created_user = User(email=email,
                        password=password,
                        name=name,
                        gender=gender,
                        profile_image=profile_image,
                        profile_image_id=profile_image_id)

    db.session.add(created_user)
    db.session.commit()

    return jsonify(
        data=model_to_dict(created_user),
        token=created_user.get_token_string()
    )

@api.route('/users/me', methods=['GET'])
@required_token
def get_user_me():
    user_data = get_user_data_from_request(request)
    print user_data
    user_id = user_data['id']
    user_me = User.query.get(user_id)

    return jsonify(
        data = model_to_dict(user_me)
    )





