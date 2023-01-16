from app import create_app


def get_wsgi_application():
    return create_app()


app = get_wsgi_application()
