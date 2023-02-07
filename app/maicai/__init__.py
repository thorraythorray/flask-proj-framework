from flask import Blueprint

from app.maicai.models import *


def create_maicai_bp():
    '''
    maicai.api.test   GET      /fla/maicai/test
    maicai.test.test  GET      /fla/test/test
    '''
    from app.maicai.apis import bp as api_bp
    maicai_bp = Blueprint("maicai", __name__)
    maicai_bp.register_blueprint(api_bp, url_prefix="/api")

    from app.maicai.clis import cli_bp
    maicai_bp.register_blueprint(cli_bp)
    return maicai_bp
