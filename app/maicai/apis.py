from flask import Blueprint

from app.exception import success
from app.db import db, to_list
from app.maicai.models import Product, Category
from utils.log import logger

bp = Blueprint("api", __name__)


@bp.route("/test", methods=["GET"])
def test():
    logger.info("test in")
    return success()


@bp.route("/prods", methods=["GET"])
def products():
    prods = db.session.query(
        Product, Category.name
    ).join(
        Category, Category.id == Product.cate_id
    ).order_by(
        Product.name
    )
    res = []
    for i in prods:
        prod_info = i[0].dump()
        prod_info["cate_name"] = i[1]
        prod_info["images"] = to_list(i[0].images)
        res.append(prod_info)
    return success(data=res)


@bp.route("/cates", methods=["GET"])
def cates():
    data = Category.query.all()
    return success(data=to_list(data))
