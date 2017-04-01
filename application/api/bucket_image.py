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

@api.route('/bucket-images', methods=['POST'])
@required_token
def upload_bucket_images():
    if dict(request.files) == {}:
        return jsonify(
            user_message = 'no image'
        ), 401
    files = request.files
    bucket_id = request.args['bucketId']
    bucket_images = []
    for image_file in files:
        image = request.files[image_file]
        image_params = upload_image(image.read(), 'bucket', image.mimetype)

        storage_key = image_params[0]
        storage_url = image_params[1]

        gs_key = blobstore.create_gs_key('/gs' + storage_key)

        serving_url = images.get_serving_url(gs_key)
        created_image = BucketImage(serving_url=serving_url, storage_url=storage_url, bucket_id=bucket_id)
        db.session.add(created_image)
        db.session.commit()
        bucket_images.append(model_to_dict(created_image))

    return jsonify(
        data=bucket_images
    )

@api.route('/bucket-images', methods=['GET'])
@required_token
def get_bucket_images():
    bucket_id = request.args['bucketId']
    if bucket_id is None:
        return jsonify(
            user_message = 'no bucket id'
        ), 401

    q = db.session.query(BucketImage).filter(BucketImage.bucket_id == bucket_id)
    image_list = q.all()

    data = []

    for bucket_img in image_list:
        data.append(model_to_dict(bucket_img))

    return jsonify(
        data=data
    )





