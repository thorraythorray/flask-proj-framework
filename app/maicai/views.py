from flask import jsonify
from flask import Blueprint

from utils.log import logger

bp = Blueprint("maicai", __name__)

@bp.route("/test", methods=["GET"])
def test():
    return jsonify('ok')
