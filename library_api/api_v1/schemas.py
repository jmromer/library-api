from marshmallow import fields

from .. import ma
from ..models.request import Request


class RequestSchema(ma.SQLAlchemyAutoSchema):
    class Meta:
        model = Request
        fields = (
            'id',
            'email',
            'available',
            'timestamp',
            'title',
        )

    timestamp = fields.Method('timestamp_iso8601')

    def timestamp_iso8601(self, obj):
        return obj.timestamp.replace(microsecond=0).isoformat()


request_schema = RequestSchema()
requests_schema = RequestSchema(many=True)
