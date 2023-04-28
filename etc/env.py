import os
from dotenv import dotenv_values

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))


class EnvConf(dict):
    instance = None

    def __new__(cls, *args, **kwargs):
        if cls.instance is None:
            cls.instance = super().__new__(cls, *args, **kwargs)
        return cls.instance

    def __init__(self, defaults=None):
        dict.__init__(self, defaults or {})
        confs = dotenv_values(".flask_env")
        for k, v in confs.items():
            self[k] = v


ENV_CONF = EnvConf()

ENV = ENV_CONF.get("FLASK_ENV")

MYSQL_URI = 'mysql+mysqldb://{}:{}@{}:{}/{}?charset=utf8mb4'.format(
    ENV_CONF["MYSQL_USER"], ENV_CONF["MYSQL_PASS"], ENV_CONF["MYSQL_HOST"],
    ENV_CONF["MYSQL_PORT"], ENV_CONF["MYSQL_DB"],
)
