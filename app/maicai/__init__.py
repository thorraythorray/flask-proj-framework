from flask import Blueprint

from app.db import BaseModelMixin, db

class BaseModel(db.Model, BaseModelMixin):
    __applabel__ = 'maicai'
    __abstract__ = True
