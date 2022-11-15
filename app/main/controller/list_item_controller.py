from flask import request
from flask_restplus import Resource

from app.main.util.decorator import token_required

from ..dto.listItemDto import ListItemDto
from ..service.list_item_service import add_item, get_all_lists_and_item, delete_a_list_item

api = ListItemDto.api
_item_list = ListItemDto.item_list

@api.route('/')
@api.header('Authorization', 'Bearer Token')
class TodoListItem(Resource):
    @api.doc('list_of_all_user_todo_list')
    # @api.marshal_list_with(_list, envelope='data')
    @token_required
    def get(self, user):
        """List all user todo list"""
        return get_all_lists_and_item(user)

    @api.response(201, 'Todo item successfully add.')
    @api.doc('add a new item todo list')
    @api.expect(_item_list, validate=True)
    @token_required
    def post(self, user):
        """add a new todo list item """
        data = request.json
        data["user"] = user
        return add_item(data=data)

@api.route('/<list_id>/<item_id>')
@api.param('list_id', 'The todo identifier')
@api.param('item_id', 'The item identifier')
@api.header('Authorization', 'Bearer Token')
class TodoList(Resource):
    @api.response(200, 'Todo successfully deleted.')
    @api.doc('delete an existing user todo')
    @token_required
    def delete(self, list_id, item_id, user):
        """delete a todo given its identifier"""
        return delete_a_list_item(list_id, item_id)