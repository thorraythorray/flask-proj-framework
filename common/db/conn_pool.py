from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from sqlalchemy.pool import QueuePool
from redis import Redis

from etc.config import envconf, SQLALCHEMY_DATABASE_URI
from util.singleton import singleton


@singleton
class RedisDBClient:
    def __init__(self, params):
        self.host = params["REDIS_HOST"]
        self.port = params["REDIS_PORT"]
        self.db = params["REDIS_DB"]
        self.password = params.get("REDIS_PWD", None)
        self.redis_db = params.get("REDIS_DB", 1)
        self.redis = Redis.from_url(f"redis://:{self.password}@{self.host}:{self.port}/{self.redis_db}")  # pylint: disable=syntax-error

redis_pool = RedisDBClient(envconf).redis


def get_mysql_session():
    return sessionmaker(create_engine(  # pylint: disable=invalid-name
        SQLALCHEMY_DATABASE_URI,
        pool_recycle=3600,
        pool_size=10,
        isolation_level="READ COMMITTED",
        poolclass=QueuePool,
    ))


mysql_session = get_mysql_session()
