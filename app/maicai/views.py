from flask import jsonify, Blueprint

bp = Blueprint("admin", __name__)


@bp.route("/login", methods=["POST"])
def test():
    return jsonify('ok')
