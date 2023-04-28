from flask import Flask
from flask_cors import CORS
from flask_migrate import Migrate, MigrateCommand

from etc.globals import ENV_CONF, MYSQL_URI


def register_blueprints(_app):
    from app.mc import create_bp as mc_bp
    _app.register_blueprint(mc_bp(), url_prefix='/mc')


def apply_cors(_app):
    CORS(_app, resources={"/*": {"origins": "*"}})


def apply_migrate(_app):
    from app.db import db
    db.init_app(_app)
    migrate = Migrate()
    migrate.init_app(_app, db=db, command=MigrateCommand)


def _load_app_config(_app):
    _app.config.update(ENV_CONF)
    _app.config['SQLALCHEMY_DATABASE_URI'] = MYSQL_URI


def create_app():
    _app = Flask(__name__)
    _load_app_config(_app)
    register_blueprints(_app)
    apply_migrate(_app)
    apply_cors(_app)
    # 注册cli
    from manager import manager_cli
    _app.cli.add_command(manager_cli)
    return _app
