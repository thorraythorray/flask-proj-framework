from flask import Blueprint

from app.maicai.views import bp as bp1


def create_bp():
    maicai = Blueprint("maicai", __name__)
    _bp = maicai.register_blueprint(bp1, url_prefix="/v1")
    return _bp
