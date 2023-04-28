
import copy

from app.orm_db import db
from app.mc import models as m


def mock_init_data():
    mock_data = {
        "category": [
            {
                "name": "水果",
                "img_url": "https://pic4.zhimg.com/459a876ffd857b3f7aacbfe122716773_r.jpg"
            },
			{
                "name": "蔬菜",
                "img_url": "https://img95.699pic.com/photo/50105/7941.jpg_wh860.jpg"
            },
			{
                "name": "玩具",
                "img_url": "https://pic1.zhimg.com/v2-a1e7a862cf94277450869e14f0101e7b_b.jpg"
            },
			{
                "name": "零食",
                "img_url": "https://img.zcool.cn/community/01b0265b21c5faa80121bbec68d3c2.jpg@1280w_1l_2o_100sh.jpg"
            },
			{
                "name": "饮品",
                "img_url": "https://pic4.zhimg.com/v2-b8e5792b08f6a6c4a6635ea3a51c9e87_r.jpg"
            },
			{
                "name": "特色",
                "img_url": "https://img.zcool.cn/community/01fc9d5a0419c9a801204a0eb3e069.jpg@1280w_1l_2o_100sh.jpg"
            },
        ],
        "product": [
            {
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
                "name": "德芙",
                "sell_price": 1.2,
                "orig_price": 2.2,
                "stock": 99,
				"img_url": "https://img.alicdn.com/bao/uploaded/i4/6000000000386/O1CN015liRRP1Eiph3z8BBE_!!6000000000386-0-picassoopen.jpg_160x160.jpg",
				"img_details": '["https://img.alicdn.com/imgextra/i4/2200627596160/O1CN01wFbcjr1vNKZQExHB2_!!2200627596160-0-scmitem6000.jpg", \
                    "https://img.alicdn.com/imgextra/i1/2200627596160/O1CN017Ka07W1vNKZSjg7LN_!!2200627596160-0-scmitem6000.jpg", \
				"https://img.alicdn.com/imgextra/i4/2200627596160/O1CN01Dk8PIG1vNKZUl0vfp_!!2200627596160-0-scmitem6000.jpg"]'
            },
			{
                "name": "士力架",
                "sell_price": 1.2,
                "orig_price": 2.2,
                "stock": 99,
				"img_url": "https://img.alicdn.com/bao/uploaded/i4/6000000000577/O1CN01uvQAlM1G8JLMlSx7q_!!6000000000577-0-picassoopen.jpg_160x160.jpg",
				"img_details": '["https://img.alicdn.com/imgextra/i2/2200627596160/O1CN01VV6VnC1vNKXgF32Eg_!!2200627596160-0-scmitem6000.jpg", \
                    "https://img.alicdn.com/imgextra/i4/2200627596160/O1CN01mHqzSJ1vNKXdWO2TS_!!2200627596160-0-scmitem6000.jpg", \
				"https://img.alicdn.com/imgextra/i3/2200627596160/O1CN01D0ly6e1vNKXdWLUS1_!!2200627596160-0-scmitem6000.jpg"]'
            },
			{
                "name": "费列罗",
                "sell_price": 1.2,
                "orig_price": 2.2,
                "stock": 99,
				"img_url": "https://img.alicdn.com/bao/uploaded/i4/6000000006520/O1CN01ovm51K1y2D9tWuWiE_!!6000000006520-0-picassoopen.jpg_160x160.jpg",
				"img_details": '["https://img.alicdn.com/imgextra/i3/3596655575/O1CN01SyMhMT1r3OdEWcZeb_!!3596655575-0-scmitem6000.jpg", \
                    "https://img.alicdn.com/imgextra/i3/3596655575/O1CN017K4Zof1r3OeEDbtDy_!!3596655575-0-scmitem6000.jpg", \
				"https://img.alicdn.com/imgextra/i3/3596655575/O1CN01TYjQOv1r3OdE3Kv9M_!!3596655575-0-scmitem6000.jpg"]'
            }
        ]
    }


    db.session.bulk_insert_mappings(
        m.Category,
        mock_data.get("category")
    )

    db.session.commit()
    cate_cnt = db.session.query(
        m.Category
    ).count()

    prods_insert_list = []
    for idx in range(cate_cnt):
        for p in mock_data.get("product"):
            item = copy.copy(p)
            item["cate_id"] = idx + 1
            prods_insert_list.append(item)

    db.session.bulk_insert_mappings(
        m.Product,
        prods_insert_list
    )
    db.session.commit()
