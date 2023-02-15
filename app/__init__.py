from flask import Flask
from flask_cors import CORS
from flask_migrate import Migrate, MigrateCommand

from etc.globals import ENV_CONF, MYSQL_URI


def register_blueprints(_app):
    from app.maicai import create_maicai_bp
    _app.register_blueprint(create_maicai_bp(), url_prefix='/fla/mc')


def apply_cors(_app):
    CORS(_app, resources={"/*": {"origins": "*"}})


def apply_migrate(_app):
    from app.db import db
    db.init_app(_app)
    migrate = Migrate()
    migrate.init_app(_app, db=db, command=MigrateCommand)


def load_app_config(_app):
    _app.config.update(ENV_CONF)
    _app.config['SQLALCHEMY_DATABASE_URI'] = MYSQL_URI


def create_app():
    _app = Flask(__name__)
    load_app_config(_app)
    register_blueprints(_app)
    apply_migrate(_app)
    apply_cors(_app)
    return _app
