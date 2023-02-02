from flask import jsonify
from flask import Blueprint

from utils.log import logger

bp = Blueprint("maicai", __name__, url_prefix='/v1/api')
print(222)

@bp.route("/test", methods=["GET"])
def test():
    print(333)
    logger.info(987654)
    return jsonify('ok')
