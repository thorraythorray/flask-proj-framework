from flask import Flask
from flask_cors import CORS

from etc.config import conf
from app.maicai import create_bp as maicai_bp


def register_blueprints(app):
    app.register_blueprint(maicai_bp(), url_prefix="/maicai")


def apply_cors(app):
    CORS(app, resources={"/*": {"origins": "*"}})


def create_app():
    app = Flask(__name__)
    register_blueprints(app)
    apply_cors(app)
    app.conf.update(conf)
    return app
