from flask import Flask

from app.maicai import create_bp as maicai_bp


def register_blueprints(app):
    app.register_blueprint(maicai_bp(), url_prefix="/maicai")


def create_app():
    app = Flask(__name__)
    register_blueprints(app)
    return app
