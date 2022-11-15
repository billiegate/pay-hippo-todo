import werkzeug
werkzeug.cached_property = werkzeug.utils.cached_property
from flask_restplus import Api
from flask import Blueprint

from .main.controller.user_controller import api as user_ns
from .main.controller.auth_controller import api as auth_ns
from .main.controller.item_controller import api as item_ns
from .main.controller.list_controller import api as list_ns
from .main.controller.list_item_controller import api as list_item_ns

blueprint = Blueprint('api', __name__)

api = Api(blueprint,
          title='TODO LIST',
          version='1.0',
          description='a todo list containing items web services'
          )

api.add_namespace(user_ns, path='/user')
api.add_namespace(auth_ns)
api.add_namespace(item_ns, path='/item')
api.add_namespace(list_ns, path='/list')
api.add_namespace(list_item_ns, path='/list-item')