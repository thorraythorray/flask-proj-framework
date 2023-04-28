from flask import Blueprint

from app.mc.models import *


def create_bp():
    """注册二级路由

    Returns:
        _type_: _description_
    """
    master_bp = Blueprint("mc", __name__)
    # 注册二级路由
    from app.mc import api
    master_bp.register_blueprint(api.bp)
    return master_bp
