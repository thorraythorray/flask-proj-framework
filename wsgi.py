from app import create_app


def get_wsgi_application():
    return create_app()

application = get_wsgi_application()
