from flask import Flask,render_template
from app import app

# Views
@app.route('/')
def index():

    '''
    View root page function that returns the index page and its data
    '''
<<<<<<< HEAD
    return render_template('home.html','login.html')

 
=======
    return render_template('home.html','login.html')
>>>>>>> dev
