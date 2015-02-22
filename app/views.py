"""
Flask Documentation:     http://flask.pocoo.org/docs/
Jinja2 Documentation:    http://jinja.pocoo.org/2/documentation/
Werkzeug Documentation:  http://werkzeug.pocoo.org/documentation/

This file creates your application.
"""
from app import db
from app import app
from flask import render_template, request, redirect, url_for
import smtplib  
import time
import sqlite3
from app.models import Profiles
from forms import CreateUserForm

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

#my functions  
def timeinfo():
    return time.strftime("%a, %d %b %Y")
  
def createID():
    return time.strftime("%y%j%H%M%S")
  
#insert profile roots
@app.route('/profile/', methods=['POST','GET'])
def profile():
    form = CreateUserForm()
    if request.method == "POST" and form.validate():
      userid = createID()#generate user id
      datecreated = timeinfo()#gets today's date
      user = Profiles(userid, form.username.data, form.firstname.data, \
                      form.lastname.data, form.age.data, form.gender.data, datecreated)
      db.session.add(user)
      db.session.commit()
      return redirect(url_for('show_user', userid=userid))
    else:
        return render_template('profile.html', form=form)  
  

@app.route('/profile/<userid>')
def show_user(userid):
    user = Profiles.query.filter_by(userid=userid).first_or_404()
    return render_template('userprofile.html', user=user)

  
@app.route('/profiles/')
def show_users():
    users = Profiles.query.all()
    return render_template('profiles.html', users=users)

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
