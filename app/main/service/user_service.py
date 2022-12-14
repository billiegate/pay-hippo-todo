import uuid
import datetime
from app.main import db
from app.main.model.user import User

def save_new_user(data):
    user = User.query.filter_by(email=data['email']).first()
    if not user:
        new_user = User(
            public_id=str(uuid.uuid4()),
            email=data['email'],
            username=data['username'],
            password=data['password'],
            registered_on=datetime.datetime.utcnow()
        )
        save_changes(new_user)
        return generate_token(new_user)
    else:
        response_object = {
            'status': 'fail',
            'message': 'User already exists. Please Log in.',
        }
        return response_object, 409


def get_all_users():
    users = User.query.all()
    response_object = {
        'status': 'success',
        'message': 'User found.',
        'data': User.serialize_list(users)
    }
    return response_object, 200


def get_a_user(public_id):
    user = User.query.filter_by(public_id=public_id).first()
    if not user:
        response_object = {
            'status': 'fail',
            'message': 'User not found.',
            'data': None
        }
        return response_object, 404
    else:
        response_object = {
            'status': 'success',
            'message': 'User found.',
            'data': user.serialize()
        }
        return response_object, 200


def save_changes(data):
    db.session.add(data)
    db.session.commit()

def generate_token(user):
    try:
        # generate the auth token
        auth_token = user.encode_auth_token(user.id)
        response_object = {
            'status': 'success',
            'message': 'Successfully registered.',
            'data': auth_token.decode()
        }
        return response_object, 201
    except Exception as e:
        response_object = {
            'status': 'fail',
            'message': 'Some error occurred. Please try again.'
        }
        return response_object, 401