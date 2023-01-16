from flask import Flask
from flask_cors import CORS

# from etc import config
from app.maicai import bp as maicai_bp


def register_blueprints(app):
    app.register_blueprint(maicai_bp, url_prefix="/maicai")


def apply_cors(app):
    CORS(app, resources={"/*": {"origins": "*"}})


def create_app():
    app = Flask(__name__)
    register_blueprints(app)
    apply_cors(app)
    # app.conf.update(config.conf)
    return app
