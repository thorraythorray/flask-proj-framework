from flask import jsonify, Blueprint

from app.maicai import bp

child = Blueprint("maicai_view", __name__)
bp.register_blueprint(child, url_prefix="/api")


@bp.route("/login", methods=["POST"])
def test():
    return jsonify('ok')
