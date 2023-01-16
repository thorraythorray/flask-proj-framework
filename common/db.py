from multiprocessing import cpu_count

import pymysql
from redis import Redis
from dbutils.pooled_db import PooledDB
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from sqlalchemy.pool import QueuePool

from utils.singleton import singleton
from etc.config import conf


@singleton
class RedisDBClient:
    def __init__(self, params):
        self.host = params["REDIS_HOST"]
        self.port = params["REDIS_PORT"]
        self.db = params["REDIS_DB"]
        self.password = params.get("REDIS_PWD", None)
        self.redis_db = params.get("REDIS_DB", 1)
        self.redis = Redis.from_url(f"redis://:{self.password}@{self.host}:{self.port}/{self.redis_db}")
redis_pool = RedisDBClient(conf).redis


@singleton
class DBClient:
    def __init__(self, params):
        self.host = params["DB_HOST"]
        self.port = params["DB_PORT"]
        self.user = params["DB_USER"]
        self.password = params["DB_PASS"]
        self.database = params["DB_NAME"]
        self.pool = PooledDB(
            creator=pymysql,
            maxconnections=(cpu_count() * 2) + 1,
            blocking=True,  # 阻塞等待
            setsession=[],
            ping=0,
            host=conf["DB_HOST"],
            port=conf["DB_PORT"],
            user=conf["DB_USER"],
            password=conf["DB_PASS"],
            database=conf["DB_NAME"],
            charset='utf8'
        )
db_pool = DBClient(conf).pool


Session = sessionmaker(create_engine(  # pylint: disable=invalid-name
    conf['SQLALCHEMY_DATABASE_URI'],
    pool_recycle=3600,
    pool_size=10,
    isolation_level="READ COMMITTED",
    poolclass=QueuePool,
))
db_session = Session()
