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
        res.append(res)
    return success(data=res)


@bp.route("/prod/<int:prod_id>", methods=["GET"])
def product_detail(prod_id):
    prod = Product.query.get(prod_id)
    return success(data=prod.dump())


@bp.route("/cates", methods=["GET"])
def cates():
    data = Category.query.all()
    return success(data=to_list(data))


@bp.route("/banner/list", methods=["GET"])
def banners():
    banner_list = [
      "https://img.zcool.cn/community/01cbe85c20c77fa8012029ac3c0e1c.jpg@1280w_1l_2o_100sh.jpg",
      "https://img.zcool.cn/community/014d3556de68de6ac72531cb2cfa4e.jpg@1280w_1l_2o_100sh.jpg",
      "https://img.zcool.cn/community/0130255779db830000018c1b4d5b69.jpg@2o.jpg",
      "https://img.zcool.cn/community/01c0115cee3ad8a80121a47058dadd.jpg@1280w_1l_2o_100sh.jpg"
    ]
    return success(data=banner_list)


@bp.route("/areas/list", methods=["GET"])
def areas():
    area_list = [
      {
        "name": "云南省昆明市昆明市五华区一二一大街298号云南师范大学",
      },
      {
        "name": "杭州市余杭塘路2318号杭州师范大学仓前校区",
      }
    ]
    return success(data=area_list)


@bp.route("/broadcast", methods=["GET"])
def broadcast():
    return success(data='年终盛会最后狂欢年末最后一次')


@bp.route("/sales", methods=["GET"])
def sales():
    prods = db.session.query(
        Product, Category.name
    ).join(
        Category, Category.id == Product.cate_id
    ).order_by(
        Product.name
    )
    sell_list = []
    for i in prods:
        prod_info = i[0].dump()
        prod_info["cate_name"] = i[1]
        sell_list.append(prod_info)
    res = {
        "sell_list": sell_list,
        "start_tm": "2023-02-20 00:00:00",
        "end_tm": "2023-02-27 00:00:00",
    }
    return success(data=res)
