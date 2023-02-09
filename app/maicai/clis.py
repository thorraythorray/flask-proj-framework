
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
                "name": "分类1",
                "img_url": "https://tse1-mm.cn.bing.net/th/id/OET.67f5a59611e34cf99a924e0e0a87791c?w=272&h=272&c=7&rs=1&o=5&dpr=1.1&pid=1.9"
            }
        ],
        "product": [
            {
                "id": 1,
                "cate_id": 1,
                "name": "商品1",
                "sell_price": 1.2,
                "orig_price": 2.2,
                "stock": 99,
            },
            {
                "id": 2,
                "cate_id": 1,
                "name": "商品2",
                "sell_price": 1.2,
                "orig_price": 2.2,
                "stock": 99,
            }
        ],
        "prodimages": [
            {
                "prod_id": 1,
                "img_url": "https://tse1-mm.cn.bing.net/th/id/OET.af47b77222b24dc4a251d7c73bb36f8f?w=135&h=272&c=7&rs=1&o=5&dpr=1.1&pid=1.9",
                "master": True
            },
            {
                "prod_id": 2,
                "img_url": "https://tse1-mm.cn.bing.net/th/id/OET.46c0a9e770dc46f782902bd706ff1b34?w=135&h=135&c=7&rs=1&o=5&dpr=1.1&pid=1.9",
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
