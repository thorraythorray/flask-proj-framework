from flask import Blueprint

from app.db import BaseModelMixin, db


bp = Blueprint("maicai", __name__, url_prefix='/v1')

class BaseModel(db.Model, BaseModelMixin):
    __applabel__ = 'maicai'
    __abstract__ = True
