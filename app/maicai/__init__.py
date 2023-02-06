from flask import Blueprint

from app.db import BaseModelMixin, db
from app.maicai.views.api import bp as api_bp
from app.maicai.views.test_api import bp as test_bp


class BaseModel(db.Model, BaseModelMixin):
    __applabel__ = 'maicai'
    __abstract__ = True


def create_maicai_bp():
    maicai_bp = Blueprint("maicai", __name__)
    # maicai.api.test   GET      /fla/maicai/test
    maicai_bp.register_blueprint(api_bp, url_prefix="/maicai")
    # maicai.test.test  GET      /fla/test/test
    maicai_bp.register_blueprint(test_bp, url_prefix="/test")
    return maicai_bp


__import__('app.maicai.models', fromlist=['Product', 'Category', 'ProdImages'])
