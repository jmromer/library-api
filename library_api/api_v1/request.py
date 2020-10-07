from flask import jsonify, request

from .. import db
from ..models.request import Request
from ..schemas.request import request_schema, requests_schema
from . import api


@api.route('/request', methods=['GET'])
def get_requests():
    return 'hello world'


@api.route('/request/<int:id>', methods=['GET'])
def get_request(id):
    return 'hello world'


@api.route('/request', methods=['POST'])
def create_request():
    return 'hello world'


@api.route('/request/<int:id>', methods=['DELETE'])
def delete_request(id):
    return 'hello world'
