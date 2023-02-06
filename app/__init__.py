from flask import Flask
from flask_cors import CORS
from flask_migrate import Migrate, MigrateCommand

from etc.config import ENV_CONF, MYSQL_URI
from app.db import db


def register_blueprints(app):
    from app.maicai import create_maicai_bp
    app.register_blueprint(create_maicai_bp(), url_prefix='/fla')


def register_cli(app):
    from commands.mock import mock_cli
    app.cli.add_command(mock_cli)


def apply_cors(app):
    CORS(app, resources={"/*": {"origins": "*"}})


def apply_migrate(app):
    db.init_app(app)
    migrate = Migrate()
    migrate.init_app(app, db=db, command=MigrateCommand)


def load_app_config(app):
    app.config.update(ENV_CONF)
    app.config['SQLALCHEMY_DATABASE_URI'] = MYSQL_URI


def create_app():
    app = Flask(__name__)
    load_app_config(app)
    register_blueprints(app)
    register_cli(app)
    apply_migrate(app)
    apply_cors(app)
    return app
