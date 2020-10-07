from flask import Blueprint

api = Blueprint('api_index', __name__)

from . import index  # noqa
