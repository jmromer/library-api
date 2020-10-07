from flask import request
from flask_api import status

from .. import db
from ..models.request import Request
from . import api
from .schemas import request_schema, requests_schema


@api.route('/request', methods=['GET'])
def get_requests():
    all_requests = Request.query.all()
    return requests_schema.dump(all_requests)


@api.route('/request/<int:id>', methods=['GET'])
def get_request(id):
    req = Request.query.get(id)
    if not req:
        return '', status.HTTP_404_NOT_FOUND
    return request_schema.dump(req)


@api.route('/request', methods=['POST'])
def create_request():
    attrs = request.get_json(force=True)
    req = Request(**attrs)
    db.session.add(req)
    db.session.commit()
    return request_schema.dump(req)


@api.route('/request/<int:id>', methods=['DELETE'])
def delete_request(id):
    req = Request.query.get(id)
    if not req:
        return '', status.HTTP_404_NOT_FOUND
    db.session.delete(req)
    db.session.commit()
    return ''
