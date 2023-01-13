import os

from dotenv import load_dotenv
from flask import Flask

from etc.config import ROOT, ENV
from app.maicai import create_bp as maicai_bp


def register_blueprints(app):
    app.register_blueprint(maicai_bp(), url_prefix="/maicai")


def load_app_config(app):
    load_dotenv(os.path.join(ROOT, "app/config/{env}.env").format(env=ENV))
    app.config.from_object("app.config.{env}.{Env}Config".format(env=env, Env=env.capitalize()))


def create_app():
    app = Flask(__name__)
    register_blueprints(app)
    return app
