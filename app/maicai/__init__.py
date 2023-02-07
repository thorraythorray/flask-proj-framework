from flask import Blueprint


def create_maicai_bp():
    '''
    maicai.api.test   GET      /fla/maicai/test
    maicai.test.test  GET      /fla/test/test
    '''
    from app.maicai.views.api import bp as api_bp
    from app.maicai.views.test_api import bp as test_bp
    maicai_bp = Blueprint("maicai", __name__)
    maicai_bp.register_blueprint(api_bp, url_prefix="/api")
    maicai_bp.register_blueprint(test_bp, url_prefix="/test")

    from app.maicai.cli import cli_bp
    maicai_bp.register_blueprint(cli_bp)
    return maicai_bp


__import__('app.maicai.models', fromlist=['Product', 'Category', 'ProdImages'])
