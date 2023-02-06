import click

from flask.cli import AppGroup

from app.db import db
from app.maicai import models as m

mock_cli = AppGroup("mock")

@mock_cli.command("test")
# @click.option("--force", is_flag=True, help="Create after drop.")
@click.argument("name")
def test_cli(name):
    print(name)


@mock_cli.command("test")
def mock_maicai():
    mock_data = {
        "cates": [
            {
                "id": 1,
                "name": "xx",
                "img_url": ""
            }
        ],
        "products": [
            {
                "id": 1,
                "cate_id": 1,
                "name": "xx",
                "sell_price": 1.2,
                "orig_price": 2.2,
                "stock": 99,
            }
        ],
        "prodimages": [
            {
                "prod_id": 1,
                "img_url": "",
                "master": True
            },
            {
                "prod_id": 1,
                "img_url": "",
            }
        ]
    }
    db.session.execute("truncate table maicai_category")
    db.session.bulk_insert_mappings(
                    m.Category,
                    mock_data.get("cates")
                )

    db.session.execute("truncate table maicai_product")
    db.session.bulk_insert_mappings(
                    m.Product,
                    mock_data.get("products")
                )

    db.session.execute("truncate table maicai_prodimages")
    db.session.bulk_insert_mappings(
                    m.ProdImages,
                    mock_data.get("prodimages")
                )
    db.session.commit()
