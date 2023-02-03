from flask import jsonify
# from flask import Blueprint

from utils.log import logger
from app.maicai import bp

# bp = Blueprint("api", __name__)

@bp.route("/test", methods=["GET"])
def test():
    return jsonify('ok')
