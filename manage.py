from app import app
# from app.models import db 
# from flask_script import Manager,Server

# from  flask_migrate import Migrate, MigrateCommand
# # Creating app instance
# app = create_app('development')





# migrate = Migrate(app,db)
# manager.add_command('db',MigrateCommand)
# manager = Manager(app)
# manager.add_command('server',Server)


if __name__ == '__main__':
    app.run(debug=True)