from flask import request
from flask_restplus import Resource

from app.main.util.decorator import token_required

from ..dto.listDto import ListDto
from ..service.list_service import save_new_list, get_all_lists, get_a_list, update_a_list, delete_a_list, duplicate

api = ListDto.api
_list = ListDto._list


@api.route('/')
@api.header('Authorization', 'Bearer Token')
class TodoList(Resource):
    @api.doc('list_of_all_user_todo_list')
    # @api.marshal_list_with(_list, envelope='data')
    @token_required
    def get(self, user):
        """List all user todo list"""
        return get_all_lists(user)

    @api.response(201, 'Todo successfully created.')
    @api.doc('create a new user todo list')
    @api.expect(_list, validate=True)
    @token_required
    def post(self, user):
        """Creates a new todo list """
        data = request.json
        data["user"] = user
        return save_new_list(data=data)


@api.route('/<id>')
@api.param('id', 'The todo identifier')
@api.header('Authorization', 'Bearer Token')
class Todo(Resource):
    @api.doc('get a todo list')
    # @api.marshal_with(_list)
    @token_required
    def get(self, id, user):
        """get a todo given its identifier"""
        return get_a_list(id)

    @api.response(201, 'Todo successfully duplicated.')
    @api.doc('duplicate an existing user todo list')
    @token_required
    def post(self, id, user):
        """Duplicates an existing todo list """
        return duplicate(id)

    @api.response(200, 'Todo successfully updated.')
    @api.doc('updates an existing user todo')
    @api.expect(_list, validate=True)
    @token_required
    def put(self, id):
        """updates a todo given its identifier"""
        data = request.json
        return update_a_list(id, data=data)

    @api.response(200, 'Todo successfully deleted.')
    @api.doc('delete an existing user todo')
    @token_required
    def delete(self, id, user):
        """get a todo given its identifier"""
        return delete_a_list(id)