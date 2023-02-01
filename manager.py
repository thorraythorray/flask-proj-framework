from flask_script import Manager
from flask_migrate import MigrateCommand, upgrade

from app import create_app


app = create_app()
manager = Manager(app)
manager.add_command('db', MigrateCommand)

@manager.command
def deploy():
    upgrade()

if __name__ == '__main__':
    manager.run()
 