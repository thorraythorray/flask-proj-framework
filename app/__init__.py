from flask import Flask
from flask_cors import CORS
from flask_migrate import Migrate, MigrateCommand

from etc.config import SQLALCHEMY_DATABASE_URI
from manager import manager_cli


def register_blueprints(_app):
    from app.mc import create_bp as mc_bp
    _app.register_blueprint(mc_bp(), url_prefix='/mc')


def apply_cors(_app):
    CORS(_app, resources={"/*": {"origins": "*"}})


def apply_migrate(_app):
    from app.orm_db import db
    db.init_app(_app)
    migrate = Migrate()
    migrate.init_app(_app, db=db, command=MigrateCommand)


def _load_app_config(_app):
    _app.config['SQLALCHEMY_DATABASE_URI'] = SQLALCHEMY_DATABASE_URI


def create_app():
    _app = Flask(__name__)
    _load_app_config(_app)

    # 注册蓝图
    register_blueprints(_app)

    # 注册app
    apply_migrate(_app)
    apply_cors(_app)

    # 注册cli
    _app.cli.add_command(manager_cli)
    return _app
