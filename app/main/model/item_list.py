from .. import db

item_list = db.Table('item_list',
                    db.Column('list_id', db.Integer, db.ForeignKey('list.id')),
                    db.Column('item_id', db.Integer, db.ForeignKey('item.id'))
                )