import uuid
import datetime

from app.main import db
from app.main.model.list import List
from app.main.model.item import Item


def save_new_list(data):
    new_list = List(
        title=data['title'],
        user_id=data['user']['id'],
        created_on=datetime.datetime.utcnow(),
        updated_on=datetime.datetime.utcnow()
    )

    if data['items'] and len(data['items']) > 0:
        for id in data['items']:
            item = Item.query.filter_by(id=id).first()
            if item:
                new_list.items.append(item)

    save_changes(new_list)
    
    response_object = {
        'status': 'success',
        'message': 'Successfully created list.',
        'data': new_list.serialize()
    }
    return response_object, 201

def duplicate(id):
    _list = List.query.filter_by(id=id).first()
    new_list = List(
        title=_list.title,
        user_id=_list.user_id,
        created_on=datetime.datetime.utcnow(),
        updated_on=datetime.datetime.utcnow()
    )
    for item in _list.items:
        new_list.items.append(item)

    save_changes(new_list)
    response_object = {
        'status': 'success',
        'message': 'Successfully duplicated item.',
        'data': new_list.serialize()
    }
    return response_object, 201


def get_all_lists(user):
    lists = List.query.filter_by(user_id=user['id'])
    response_object = {
        'status': 'success',
        'message': 'Lists found.',
        'data': List.serialize_list(lists)
    }
    return response_object, 200


def get_a_list(id):
    list = List.query.filter_by(id=id).first()
    if not list:
        response_object = {
            'status': 'fail',
            'message': 'List not found',
            'data': None
        }
        return response_object, 404

    response_object = {
        'status': 'success',
        'message': 'List found',
        'data': list.serialize()
    }
    return response_object, 404


def save_changes(data):
    db.session.add(data)
    db.session.commit()

def add_item(data): 
    list = List.query.filter_by(id=data['list_id']).first()
    item = Item.query.filter_by(id=data['item_id']).first()

    if not list:
        response_object = {
            'status': 'fail',
            'message': 'List not found',
        }
        return response_object, 404
    
    if not item:
        response_object = {
            'status': 'fail',
            'message': 'Item not found.',
        }
        return response_object, 404

    list.items.append(item)

def update_a_list(id, data):
    existing_list = List.query.filter_by(id=id).first()
    if not existing_list:
        response_object = {
            'status': 'failed',
            'message': 'todo list not found',
            'data': None
        }
        return response_object, 404
    existing_list.value = data['value']
    db.session.commit()
    response_object = {
        'status': 'success',
        'message': 'Successfully update list.',
        'data': existing_list.serialize()
    }
    return response_object, 200

def delete_a_list(id):
    existing_list = List.query.filter_by(id=id).first()
    if not existing_list:
        response_object = {
            'status': 'failed',
            'message': 'todo list not found',
            'data': None
        }
        return response_object, 404
    db.session.delete(existing_list)
    db.session.commit()
    response_object = {
        'status': 'success',
        'message': 'Successfully deleted list.',
        'data': None
    }
    return response_object, 200