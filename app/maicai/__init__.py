from flask import Blueprint

from app.db import BaseModelMixin, db


class BaseModel(db.Model, BaseModelMixin):
    __applabel__ = 'maicai'
    __abstract__ = True


def create_maicai_bp():
    maicai_bp = Blueprint("maicai", __name__, url_prefix='/maicai')
    from app.maicai.views import bp as api_bp
    maicai_bp.register_blueprint(api_bp, url_prefix="/api")
    return maicai_bp
