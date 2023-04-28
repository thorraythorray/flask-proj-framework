from datetime import datetime

from flask_sqlalchemy import SQLAlchemy
from sqlalchemy import Column, Integer, DateTime
from sqlalchemy.ext.declarative import declared_attr

db = SQLAlchemy()


class BaseModel(db.Model):
    __abstract__ = True

    @declared_attr
    def __tablename__(cls):  # pylint: disable=no-self-argument
        return cls.__name__.lower()

    id = Column(Integer, primary_key=True, autoincrement=True)
    created = Column(DateTime, nullable=False, default=datetime.now)
    updated = Column(DateTime, nullable=False, default=datetime.now, onupdate=datetime.now)

    @classmethod
    def create(cls, **kwargs):
        self = cls()
        for key, val in kwargs.items():
            if hasattr(self, key):
                setattr(self, key, val)
        db.session.add(self)
        db.session.commit()
        return self

    def update(self, **kwargs):
        for key, val in kwargs.items():
            if hasattr(self, key):
                setattr(self, key, val)
        db.session.add(self)
        db.session.commit()
        return self

    def delete(self):
        db.session.delete(self)
        db.session.commit()

    def dump(self):
        data = {}
        for column in self.__table__.columns:
            value = getattr(self, column.name, None)
            data[column.name] = value
        return data


def to_dict(model, excludes=None, includes=None):
    columns = set(c.name for c in model.__table__.columns) \
        - set(c.name for c in getattr(model, "_excludes_", [])) \
        | set(getattr(model, "_includes_", []))
    if excludes:
        columns -= set(c for c in excludes)
    if includes:
        columns = set(c for c in includes)
    data = {}
    for column in columns:
        value = getattr(model, column, None)
        if isinstance(value, db.Model):
            value = to_dict(value)
        data[column] = value
    return data


def to_list(query, excludes=None, includes=None):
    return [to_dict(item, excludes=excludes, includes=includes) for item in query]
