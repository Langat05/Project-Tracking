from app import app
# from flask_script import Manager,Server

<<<<<<< HEAD
# # Creating app instance
# app = create_app('development')
=======
# Creating app instance
# app = create_app('development')
# app = create_app('production')
>>>>>>> a556091e54bcae2e4b3e5623ba407cbe8e297aca

# manager = Manager(app)
# manager.add_command('server',Server)


if __name__ == '__main__':
    app.run(debug=True)