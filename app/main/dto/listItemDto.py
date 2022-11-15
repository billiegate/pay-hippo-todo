from flask_restplus import Namespace, fields


class ListItemDto:
    api = Namespace('item_list', description='list items related operations')
    item_list = api.model('item_list', {
        'item': fields.Integer(required=True, description='ID of the item to add'),
        'list': fields.Integer(required=True, description='ID of the list to add')
    })