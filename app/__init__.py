


def register_blueprints(app):
    from app.maicai.urls import blueprint as maicai_bp
    app.register_blueprint(maicai_bp(), url_prefix="/maicai")


def create_app():
    from flask import Flask
    app = Flask(__name__)
    register_blueprints(app)
    return app
