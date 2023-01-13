from flask import Blueprint

from app.maicai.views.admin import admin_bp


def create_bp():
    maicai = Blueprint("maicai", __name__)
    bp = maicai.register_blueprint(admin_bp, url_prefix="/v1")
    return bp
