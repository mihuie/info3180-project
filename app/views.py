"""
Flask Documentation:     http://flask.pocoo.org/docs/
Jinja2 Documentation:    http://jinja.pocoo.org/2/documentation/
Werkzeug Documentation:  http://werkzeug.pocoo.org/documentation/

This file creates your application.
"""
from app import db
from app import app
from flask import render_template, request, redirect, url_for, flash, g
import smtplib  
import time
import sqlite3
from app import app
from app.models import Profiles


app.secret_key = 'my superrr dupper secret_key'

###
# Routing for your application.
###

@app.route('/')
def home():
    """Render website's home page."""
    return render_template('home.html')


@app.route('/about/')
def about():
    """Render the website's about page."""
    return render_template('about.html')

#create user profile
@app.route('/profile/')
def profile():
    return render_template('profile.html')
  
def timeinfo():
    return time.strftime("%a, %d %b %Y")
  
def createID():
    return time.strftime("%y%j%H%M%S")

@app.route('/profiles/', methods=['POST'])
def userprofile():
  
    userid = createID()
    username = request.form['username']
    firstname = request.form['fname']
    lastname = request.form['lname']
    age = request.form['age']
    gender = request.form['sex']
    date_created = timeinfo()
    
#     newuser = User(userid, username, firstname, lastname, age, gender, date_created)
#     db.session.add(newuser)
#     db.session.commit()

    return render_template('userprofile.html', userid=userid, username=username, \
                           firstname=firstname, lastname=lastname, age=age, \
                           gender=gender, date_created=date_created)
  
###
# The functions below should be applicable to all Flask apps.
###

@app.route('/<file_name>.txt')
def send_text_file(file_name):
    """Send your static text file."""
    file_dot_text = file_name + '.txt'
    return app.send_static_file(file_dot_text)


@app.after_request
def add_header(response):
    """
    Add headers to both force latest IE rendering engine or Chrome Frame,
    and also to cache the rendered page for 10 minutes.
    """
    response.headers['X-UA-Compatible'] = 'IE=Edge,chrome=1'
    response.headers['Cache-Control'] = 'public, max-age=600'
    return response


@app.errorhandler(404)
def page_not_found(error):
    """Custom 404 page."""
    return render_template('404.html'), 404


if __name__ == '__main__':
    app.run(debug=True,host="0.0.0.0",port="8888")
