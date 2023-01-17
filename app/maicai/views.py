from flask import jsonify

from app.maicai import bp

bp.register_blueprint("maicai_view", url_prefix="/api")


@bp.route("/login", methods=["POST"])
def test():
    return jsonify('ok')
