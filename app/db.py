from datetime import datetime

from flask_sqlalchemy import SQLAlchemy
from sqlalchemy import Column, Integer, DateTime, create_engine
from sqlalchemy.ext.declarative import declared_attr
from sqlalchemy.orm import sessionmaker, scoped_session

from etc.globals import MYSQL_URI

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


def get_mysql_session():
    db_engine = create_engine(
        MYSQL_URI,
        pool_recycle=3600, pool_size=3000,
        isolation_level="READ COMMITTED"
    )
    db_session = scoped_session(sessionmaker(db_engine))
    return db_session()
