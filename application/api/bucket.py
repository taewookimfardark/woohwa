from . import api
from application import db
from application.models.bucket import UncompleteBucket
from application.models.bucket import CompleteBucket

from flask import request, jsonify
from application.lib.rest.rest_query_helper import (
    model_to_dict
)

from application.lib.rest.auth_helper import (
    get_user_data_from_request,
    required_token
)

#from application.lib.storage.cloud_storage_helper import upload_image

import json
import sys
reload(sys)
sys.setdefaultencoding('utf-8')


@api.route("/buckets/uncomplete", methods=['GET'])
def get_uncomplete_buckets():
    buckets_uncomplete = UncompleteBucket.query.all()
    query_list = []
    for bucket_uncomplete in buckets_uncomplete:
        temp = model_to_dict(bucket_uncomplete)
        query_list.append(temp)
    print(query_list)

    return jsonify(
        data = query_list
    )

@api.route('/buckets/uncomplete', methods=['POST'])
def post_uncomplete_buckets():
    request_params = request.get_json()
    userid = request_params.get('userid')
    title = request_params.get('title')
    when_month = request_params.get('when_month')
    where = request_params.get('where')
    info = request_params.get('info')
    reward = request_params.get('reward')
    status = request_params.get('status')
    iscomplete = request_params.get('iscomplete')
    excesslimit = request_params.get('excesslimit')
    uncomplete_bucket = UncompleteBucket(userid=userid,title=title,when_month=when_month,where=where,info=info,reward=reward,status=status,iscomplete=iscomplete,excesslimit=excesslimit)
    db.session.add(uncomplete_bucket)
    db.session.commit()
    return jsonify(
        data=model_to_dict(uncomplete_bucket)
    )