from flask_restplus import Namespace, fields


class ListDto:
    api = Namespace('list', description='list related operations')
    _list = api.model('list', {
        'title': fields.String(required=True, description='the content to list'),
        'items': fields.List(fields.Integer, required=False, description='ids of item to add to this list')
    })