from flask import url_for

from . import api


@api.route('/', methods=['GET'])
def get_requests():
    return {
        'api_endpoints': {
            'v1': {
                'requests': {
                    'list': {
                        'method': 'GET',
                        'path': '/api/v1/request',
                    },
                    'create': {
                        'method': 'POST',
                        'path': '/api/v1/request',
                    },
                    'retrieve': {
                        'method': 'GET',
                        'path': '/api/v1/request/:id',
                    },
                    'destroy': {
                        'method': 'DELETE',
                        'path': '/api/v1/request/:id',
                    },
                }
            }
        }
    }
