
import click

from flask import Blueprint

from app.db import db
from app.maicai import models as m

cli_bp = Blueprint("cli", __name__, cli_group="maicai")


@cli_bp.cli.command("test")
@click.argument('name')
def test_cli(name):
    print(name)


@cli_bp.cli.command("mock")
def mock_init_data():
    mock_data = {
        "category": [
            {
                "id": 1,
                "name": "水果",
                "img_url": "https://pic4.zhimg.com/459a876ffd857b3f7aacbfe122716773_r.jpg"
            },
			{
                "id": 2,
                "name": "蔬菜",
                "img_url": "https://img95.699pic.com/photo/50105/7941.jpg_wh860.jpg"
            },
			{
                "id": 3,
                "name": "玩具",
                "img_url": "https://pic1.zhimg.com/v2-a1e7a862cf94277450869e14f0101e7b_b.jpg"
            },
			{
                "id": 4,
                "name": "零食",
                "img_url": "https://img.zcool.cn/community/01b0265b21c5faa80121bbec68d3c2.jpg@1280w_1l_2o_100sh.jpg"
            },
			{
                "id": 5,
                "name": "饮品",
                "img_url": "https://pic4.zhimg.com/v2-b8e5792b08f6a6c4a6635ea3a51c9e87_r.jpg"
            },
			{
                "id": 5,
                "name": "特色",
                "img_url": "https://img.zcool.cn/community/01fc9d5a0419c9a801204a0eb3e069.jpg@1280w_1l_2o_100sh.jpg"
            },
        ],
        "product": [
            {
                "id": 1,
                "cate_id": 5,
                "name": "牛奶",
                "sell_price": 1.2,
                "orig_price": 2.2,
                "stock": 99,
				"img_url": "https://img.alicdn.com/bao/uploaded/i2/6000000003953/O1CN01H3CEa41f4WSS0QiUK_!!6000000003953-0-picassoopen.jpg_160x160.jpg",
				"img_details": '["https://img.alicdn.com/bao/uploaded/i2/6000000003953/O1CN01H3CEa41f4WSS0QiUK_!!6000000003953-0-picassoopen.jpg_160x160.jpg", \
                    "https://img.alicdn.com/imgextra/i3/2200638584267/O1CN01Q8Gjf51hOKoHetOjr_!!2200638584267-0-scmitem6000.jpg", \
                        "https://img.alicdn.com/imgextra/i4/2200638584267/O1CN01FkmNI11hOKoSp2SbY_!!2200638584267-0-scmitem6000.jpg"]'
            },
            {
                "id": 2,
                "cate_id": 1,
                "name": "商品2",
                "sell_price": 1.2,
                "orig_price": 2.2,
                "stock": 99,
            }
        ]
    }

    db.session.execute("truncate table prodimages")
    db.session.execute("truncate table product")
    db.session.execute("truncate table category")

    db.session.bulk_insert_mappings(
                    m.Category,
                    mock_data.get("category")
                )

    db.session.bulk_insert_mappings(
                    m.Product,
                    mock_data.get("product")
                )

    db.session.bulk_insert_mappings(
                    m.ProdImages,
                    mock_data.get("prodimages")
                )
    db.session.commit()
