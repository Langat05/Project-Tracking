from app import app
# from flask_script import Manager,Server


# # Creating app instance
# app = create_app('development')

# Creating app instance
# app = create_app('development')
# app = create_app('production')


# manager = Manager(app)
# manager.add_command('server',Server)


if __name__ == '__main__':
    app.run(debug=True)