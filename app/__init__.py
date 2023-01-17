from flask import Flask
from flask_cors import CORS
from flask_migrate import Migrate
from flask_sqlalchemy import SQLAlchemy

from etc.config import ENV_CONF, MYSQL_URI
from app.maicai import bp as maicai_bp

# __import__('app.maicai', fromlist=['Product'])
# __import__('app.maicai.models', fromlist=['Product', 'Category', 'ProdImages'])


def register_blueprints(app):
    app.register_blueprint(maicai_bp, url_prefix="/maicai")


def apply_cors(app):
    CORS(app, resources={"/*": {"origins": "*"}})


def apply_migrate(app):
    db = SQLAlchemy()
    db.init_app(app)
    migrate = Migrate()
    migrate.init_app(app, db=db)


def load_app_config(app):
    app.config.update(ENV_CONF)
    app.config['SQLALCHEMY_DATABASE_URI'] = MYSQL_URI


def create_app():
    app = Flask(__name__)
    load_app_config(app)
    register_blueprints(app)
    apply_migrate(app)
    apply_cors(app)
    return app
