from flask_script import Manager, upgrade
from flask_migrate import MigrateCommand

from app import create_app


app = create_app()
manager = Manager(app)
manager.add_command('db', MigrateCommand)

@manager.command
def deploy():
    upgrade()

if __name__ == '__main__':
    manager.run()
