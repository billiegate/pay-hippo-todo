import datetime

from app.main import db
from app.main.model.item import Item


def save_new_item(data):
    new_item = Item(
        text=data['text'],
        user_id=data['user']['id'],
        created_on=datetime.datetime.utcnow(),
        updated_on=datetime.datetime.utcnow()
    )
    save_changes(new_item)
    response_object = {
        'status': 'success',
        'message': 'Successfully created item.',
        'data': new_item.serialize()
    }
    return response_object, 201

def get_all_items(user):
    items = Item.query.filter_by(user_id=user['id'])
    response_object = {
        'status': 'success',
        'message': 'Items found.',
        'data': Item.serialize_list(items)
    }
    return response_object, 200


def get_an_item(id):
    return Item.query.filter_by(id=id).first()

def update_an_item(id, data):
    item = Item.query.filter_by(id=id).first()
    if not item:
        response_object = {
            'status': 'failed',
            'message': 'Item not found',
            'data': None
        }
        return response_object, 404
    item.text = data['text']
    db.session.commit()
    response_object = {
        'status': 'success',
        'message': 'Successfully updated item.',
        'data': item
    }
    return response_object, 200

def delete_an_item(id):
    item = Item.query.filter_by(id=id).first()
    if not item:
        response_object = {
            'status': 'failed',
            'message': 'Item not found',
            'data': None
        }
        return response_object, 404
    db.session.delete(item)
    db.session.commit()
    response_object = {
        'status': 'success',
        'message': 'Successfully deteled item.',
        'data': item
    }
    return response_object, 200


def save_changes(data):
    db.session.add(data)
    db.session.commit()