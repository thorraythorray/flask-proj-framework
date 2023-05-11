import os

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))


# def get_env_config():
#     return {k: v for k, v in os.environ.items()}

# envconf = get_env_config()
envconf = os.environ

ENV = envconf.get("FLASK_ENV")

SQLALCHEMY_DATABASE_URI = 'mysql+mysqldb://{}:{}@{}:{}/{}?charset=utf8mb4'.format(
    envconf.get("MYSQL_USER"), envconf.get("MYSQL_PASS"), envconf.get("MYSQL_HOST"),
    envconf.get("MYSQL_PORT"), envconf.get("MYSQL_DB"),
)
