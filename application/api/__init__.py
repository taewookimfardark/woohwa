from flask import Blueprint

api = Blueprint('api', __name__)

from . import (user, relation_user_group, group, bucket, image)
