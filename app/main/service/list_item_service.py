from app.main import db
from app.main.model.list import List
from app.main.model.item import Item
from app.main.model.item_list import item_list


def get_all_lists_and_item(user):
    lists = List.query.filter_by(user_id=user['id'])
    response_object = {
        'status': 'success',
        'message': 'Lists found.',
        'data': List.serialize_list(lists)
    }
    return response_object, 200

def add_item(data): 
    list = List.query.filter_by(id=data['list']).first()
    item = Item.query.filter_by(id=data['item']).first()

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

    db.session.commit()
    response_object = {
        'status': 'success',
        'message': 'Successfully update list.',
        'data': list.serialize()
    }
    return response_object, 200


def delete_a_list_item(list_id, item_id):
    list = List.query.filter_by(id=list_id).first()
    item = Item.query.filter_by(id=item_id).first()
    if item in list.items:
        list.items.remove(item)
        db.session.commit()
    
    response_object = {
        'status': 'success',
        'message': 'Successfully removed item.',
        'data': list.serialize()
    }
    return response_object, 200
