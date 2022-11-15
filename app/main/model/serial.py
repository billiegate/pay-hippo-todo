from sqlalchemy.inspection import inspect
from datetime import date

class Serializer(object):

    def serialize(self):
        return {c: getattr(self, c) if not isinstance(getattr(self, c), date) else getattr(self, c).strftime("%Y-%m-%d") + " " + getattr(self, c).strftime("%H:%M:%S") for c in inspect(self).attrs.keys() }

    @staticmethod
    def serialize_list(l):
        return [m.serialize() for m in l]