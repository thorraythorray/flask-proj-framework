from flask import Blueprint

from app.maicai.admin import admin_bp


def blueprint():
    maicai = Blueprint("maicai", __name__)
    maicai.register_blueprint(admin_bp, url_prefix="/v1")
    return maicai
