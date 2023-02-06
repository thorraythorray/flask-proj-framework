from flask import jsonify
from flask import Blueprint

from utils.log import logger

bp = Blueprint("api", __name__)

@bp.route("/test", methods=["GET"])
def test():
    logger.info("test in")
    return jsonify('ok')
