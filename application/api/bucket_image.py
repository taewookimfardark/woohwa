# coding: utf8
import datetime
from base64 import b64decode
from time import time
from flask import jsonify
from flask import request
from flask import current_app
import cloudstorage as gcs
from application.helper.storage.cloud_storage_helper import upload_image
from application.helper.rest.auth_helpler import get_user_data_from_request
from application.helper.rest.request_query_helper import model_to_dict
from google.appengine.api import app_identity
from google.appengine.ext import blobstore
from google.appengine.api import images
from . import api
from application import db
from application.helper.rest.auth_helpler import required_token
from application.models.bucket_image import BucketImage

@api.route('/bucket_images', methods=['POST'])
@required_token
def upload_images():
    print request.form
    if dict(request.files) == {}:
        return jsonify(
            user_message = 'no image'
        ), 401

    image = request.files['file']
    image_params = upload_image(image.read(), 'bucket', image.mimetype)

    storage_key = image_params[0]
    storage_url = image_params[1]

    print storage_key

    gs_key = blobstore.create_gs_key('/gs' + storage_key)

    serving_url = images.get_serving_url(gs_key)

    uploader_id = get_user_data_from_request(request)['id']

    created_image = BucketImage(serving_url=serving_url, storage_url=storage_url, uploader_id=uploader_id)

    db.session.add(created_image)
    db.session.commit()

    return jsonify(
        data=model_to_dict(created_image)
    )



