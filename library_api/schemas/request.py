from marshmallow_sqlalchemy import ModelSchema

from .. import ma
from ..models.request import Request


class RequestSchema(ma.Schema):
    class Meta:
        model = Request


request_schema = RequestSchema()
requests_schema = RequestSchema(many=True)
