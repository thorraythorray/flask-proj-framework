from datetime import datetime

from flask_sqlalchemy import SQLAlchemy
from sqlalchemy import Column, Integer, DateTime
from sqlalchemy.ext.declarative import declared_attr

db = SQLAlchemy()

class BaseModelMixin:

    @declared_attr
    def __tablename__(cls):  # pylint: disable=no-self-argument
        return cls.__applabel__.lower() + "_" + cls.__name__.lower()

    id = Column(Integer, primary_key=True, autoincrement=True)
    created = Column(DateTime, nullable=False, default=datetime.now)
    updated = Column(DateTime, nullable=False, onupdate=datetime.now)

    def save(self):
        db.session.add(self)
        db.session.commit()

    def delete(self):
        db.session.delete(self)
        db.session.commit()
