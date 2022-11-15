from app.main.model.serial import Serializer
from .. import db

class List(db.Model, Serializer):
    """ List Model for storing list related details """
    __tablename__ = "list"

    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    title = db.Column(db.String(255), nullable=False)
    status = db.Column(db.Boolean, nullable=False, default=False)
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'), nullable=False)
    created_on = db.Column(db.DateTime, nullable=False)
    updated_on = db.Column(db.DateTime, nullable=False)

    items = db.relationship('Item', secondary="item_list", backref=db.backref('lists'))

    def serialize(self):
        d = Serializer.serialize(self)
        i = [i.serialize() if i else '' for i in d['items']]
        u = d['user'].serialize()
        del d['user']
        del d['items']
        d['user'] = u
        d['items'] = i
        return d