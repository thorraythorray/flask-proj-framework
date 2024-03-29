# coding: utf-8
import json

from sqlalchemy import Column, Integer, VARCHAR, Text, Float

from app.orm_db import BaseModel


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
    img_url = Column(VARCHAR(255))
    img_details = Column(Text)
    desc = Column(Text)

    def dump(self):
        data = super().dump()
        if self.img_details:
            data["img_details"] = json.dumps(self.img_details)
        else:
            del data["img_details"]
        return data
