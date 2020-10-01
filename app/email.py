<<<<<<< HEAD
from flask_mail import Message
from flask import render_template
from . import mail

def mail_message(subject,template,to,**kwargs):
    sender_email = ''

    email = Message(subject, sender=sender_email, recipients=[to])
    email.body= render_template(template + ".txt",**kwargs)
    email.html = render_template(template + ".html",**kwargs)
    mail.send(email)
=======
from flask import render_template
from app import app
from threading import Thread

def send_password_reset_email(user):
    token = user.get_reset_password_token()
    send_email('[Tracking-website] Reset Your Password',
               sender=app.config['ADMINS'][0],
               recipients=[user.email],
               text_body=render_template('email/reset_password.txt',
                                         user=user, token=token),
               html_body=render_template('email/reset_password.html',
                                         user=user, token=token))

def send_async_email(app, msg):
    with app.app_context():
        mail.send(msg)      

def send_email(subject, sender, recipients, text_body, html_body):
    msg = Message(subject, sender=sender, recipients=recipients)
    msg.body = text_body
    msg.html = html_body
    Thread(target=send_async_email, args=(app, msg)).start()    
>>>>>>> 7697a7acb084532501959eeb7c1f3b4f059da74b
