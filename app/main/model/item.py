from app.main.model.serial import Serializer
from .. import db

class Item(db.Model, Serializer):
    """ Item Model for storing items that belongs to a list """
    __tablename__ = "item"

    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    text = db.Column(db.String(255), nullable=False)
    status = db.Column(db.Boolean, nullable=False, default=False)
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'), nullable=False)
    created_on = db.Column(db.DateTime, nullable=False)
    updated_on = db.Column(db.DateTime, nullable=False)

    def serialize(self):
        d = Serializer.serialize(self)
        u = d['user'].serialize()
        del d['user']
        del d['lists']
        d['user'] = u
        return d