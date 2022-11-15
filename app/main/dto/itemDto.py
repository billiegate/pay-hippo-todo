from flask_restplus import Namespace, fields


class ItemDto:
    api = Namespace('item', description='item related operations')
    item = api.model('item', {
        'text': fields.String(required=True, description='the content for the item')
    })
    # parser = api.parser()
    # parser.add_argument('authorization', type=str, help='Bearer Token', location='headers')