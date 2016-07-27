from . import api
from application import db
from application.models.user import User

from flask import request, jsonify
from application.lib.rest.rest_query_helper import (
    model_to_dict
)
from application.lib.rest.auth_helper import (
    get_user_data_from_request,
    required_token
)

from application.lib.storage.cloud_storage_helper import upload_image

import json
import sys
reload(sys)
sys.setdefaultencoding('utf-8')


@api.route("/")
def heool():
    return "hello woohwa"

@api.route("/users", methods=['GET'])
def get_users():
    users = User.query.all()
    query_list = []
    for user in users:
        temp = model_to_dict(user)
        query_list.append(temp)

    return jsonify(
        query_list
    )

