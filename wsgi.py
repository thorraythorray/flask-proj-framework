from app import create_app


def load_usr_env():
    # flask启动会自动加载.env和.flaskenv
    # load_dotenv(config)
    pass


def get_wsgi_application():
    # 加载环境变量
    load_usr_env()
    return create_app()

application = get_wsgi_application()
