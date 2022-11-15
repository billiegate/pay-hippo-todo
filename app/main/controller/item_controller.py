from flask import request
from flask_restplus import Resource

from app.main.util.decorator import token_required

from ..dto.itemDto import ItemDto
from ..service.item_service import save_new_item, get_all_items, get_an_item, update_an_item, delete_an_item

api = ItemDto.api
_item = ItemDto.item


@api.route('/')
@api.header('Authorization', 'Bearer Token')
class ItemList(Resource):
    @api.doc('list_of_all_todo_list_item')
    # @api.marshal_list_with(_item, envelope='data')
    @token_required
    def get(self, user):
        """list all todo list item"""
        return get_all_items(user)

    @api.response(201, 'item successfully created.')
    @api.doc('create a new user todo list item')
    @api.expect(_item, validate=True)
    @token_required
    def post(self, user):
        """Creates a new todo list item """
        data = request.json
        data.update({"user":user})
        return save_new_item(data=data)


@api.route('/<id>')
@api.param('id', 'The item identifier')
@api.response(404, 'item not found.')
class Item(Resource):
    @api.doc('get a todo list item')
    @api.marshal_with(_item)
    @token_required
    def get(self, id):
        """get a item given its identifier"""
        item = get_an_item(id)
        if not item:
            api.abort(404)
        else:
            return item

    @api.response(200, 'Item successfully updated.')
    @api.doc('updates an existing todo item')
    @api.expect(_item, validate=True)
    @token_required
    def put(self, id):
        """updates a todo item given its identifier"""
        data = request.json
        return update_an_item(id, data=data)

    @api.response(200, 'Item successfully deleted.')
    @api.doc('delete an existing todo item')
    @token_required
    def delete(self, id):
        """deletes a todo item given its identifier"""
        return delete_an_item(id)