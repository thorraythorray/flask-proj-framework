from flask import Blueprint

from app.db import BaseModelMixin, db
from app.maicai.views import bp as api_bp


class BaseModel(db.Model, BaseModelMixin):
    __applabel__ = 'maicai'
    __abstract__ = True


def create_maicai_bp():
    maicai_bp = Blueprint("maicai", __name__)
    maicai_bp.register_blueprint(api_bp, url_prefix="/maicai")
    return maicai_bp
