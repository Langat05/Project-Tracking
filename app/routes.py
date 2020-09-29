from flask import render_template
from app import app, db 

@app.route('/', methods=['GET', 'POST'])    
@app.route('/index', methods=['GET', 'POST'])    