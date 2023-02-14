# coding: utf-8
from sqlalchemy import Column, Integer, VARCHAR, Text, Float, Boolean

from app.db import BaseModel


PROD_STATUS = (
    (0, '上架'),
    (1, '售罄'),
    (2, '下架'),
    (3, '促销'),
)

class Category(BaseModel):
    name = Column(VARCHAR(32), nullable=False)
    img_url = Column(VARCHAR(255))
    desc = Column(Text)
    #products = relationship("Product", backref="cate", cascade="delete", primaryjoin='Category.id==Product.cate_id')


class Product(BaseModel):
    cate_id = Column(Integer, index=True, nullable=False)
    name = Column(VARCHAR(32), nullable=False)
    sell_price = Column(Float, nullable=False)
    orig_price = Column(Float, nullable=False)
    stock = Column(Integer, nullable=False, default=0)
    status = Column(Integer, default=0)
    desc = Column(Text)
    #images = relationship("ProdImages", backref="prod", cascade="delete", primaryjoin='Product.id==ProdImages.cate_id')


class ProdImages(BaseModel):
    prod_id = Column(Integer, index=True, nullable=False)
    master = Column(Boolean, default=False)
    img_url = Column(VARCHAR(255))
