from flask import Blueprint

from app.db import BaseModelMixin, db
from app.maicai.views.api import bp as api_bp
from app.maicai.views.test_api import bp as test_bp


class BaseModel(db.Model, BaseModelMixin):
    __applabel__ = 'maicai'
    __abstract__ = True


def create_maicai_bp():
    '''
    maicai.api.test   GET      /fla/maicai/test
    maicai.test.test  GET      /fla/test/test
    '''
    maicai_bp = Blueprint("mc", __name__)
    maicai_bp.register_blueprint(api_bp, url_prefix="/api")
    maicai_bp.register_blueprint(test_bp, url_prefix="/test")

    from app.maicai.cli import bp as cli_bp
    maicai_bp.register_blueprint(cli_bp)
    return maicai_bp


__import__('app.maicai.models', fromlist=['Product', 'Category', 'ProdImages'])
