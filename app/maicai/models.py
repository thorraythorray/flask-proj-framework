# coding: utf-8
from sqlalchemy import Column, Integer, VARCHAR, Text, Float

from app.maicai import BaseModel


PROD_STATUS = (
    (0, '上架'),
    (1, '售罄'),
    (2, '下架'),
    (3, '促销'),
)

class Product(BaseModel):
    name = Column(VARCHAR(32), nullable=False)
    sell_price = Column(Float, nullable=False)
    orig_price = Column(Float, nullable=False)
    stock = Column(Integer, nullable=False, default=0)
    status = Column(Integer, default=0)
    desc = Column(Text)


class Category(BaseModel):
    name = Column(VARCHAR(32), nullable=False)
    img_url = Column(VARCHAR(255))
    desc = Column(Text)


class ProdImages(BaseModel):
    name = Column(VARCHAR(32))
    prod_id = Column(Integer, nullable=False, index=True)
    img_url = Column(VARCHAR(255))
