<<<<<<< HEAD
<<<<<<< HEAD
from  flask_migrate import Migrate, MigrateCommand
=======
from app import create_app
from flask_script import Manager,Server

# Creating app instance
app = create_app('development')

manager = Manager(app)
manager.add_command('server',Server)


if __name__ == '__main__':
    manager.run(Debug=True)
>>>>>>> 7697a7acb084532501959eeb7c1f3b4f059da74b
=======
>>>>>>> dev
