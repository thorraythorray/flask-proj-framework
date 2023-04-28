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

    # 添加cli
    from app.mc import cli
    master_bp.register_blueprint(cli.cli)
    return master_bp
