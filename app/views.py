"""
Flask Documentation:     http://flask.pocoo.org/docs/
Jinja2 Documentation:    http://jinja.pocoo.org/2/documentation/
Werkzeug Documentation:  http://werkzeug.pocoo.org/documentation/

This file creates your application.
"""
from app import db
from app import app
from flask import render_template, request, redirect, url_for, flash
import smtplib  
import time
import sqlite3
from app.models import Profiles
from forms import CreateUserForm
from werkzeug import secure_filename
from flask import jsonify,session

app.secret_key = 'my superrr dupper secret_key'
UPLOAD_FOLDER = 'app/static/img/'
app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER

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
  
def not_found():
    message = {
            'status': 404,
            'message': 'Not Found: ' + request.url,
    }
    resp = jsonify(message)
    resp.status_code = 404

    return resp
  
#insert profile roots
@app.route('/profile/', methods=['POST','GET'])
def profile():
    form = CreateUserForm()
    if request.method == "POST" and form.validate():
      
       if (Profiles.query.filter_by(username = form.username.data).first() is None):
           
          userid = createID()#generate user id
          profile_add_on = timeinfo()#gets today's date
          
          extn = (form.image.data.filename).rsplit('.', 1)[1]
          filename = secure_filename(userid +'.'+ extn)
          form.image.data.save(UPLOAD_FOLDER + filename)
          imagelocations = 'img/' + filename
          user = Profiles(userid, form.username.data, form.firstname.data, \
                          form.lastname.data, form.age.data, form.gender.data, \
                          profile_add_on, imagelocations)
          db.session.add(user)
          db.session.commit()
          return redirect(url_for('show_user', userid=userid ))
       else:
          flash('Username already taken.')
          return render_template('profile.html', form=form)       
    else:
        return render_template('profile.html', form=form)  
  
  
@app.route('/profile/<userid>', methods =['GET','POST'])
def show_user(userid):
    user = Profiles.query.filter_by(userid=userid).first_or_404()
    
#     if request.headers['Content-Type'] == 'application/json': 
#       return jsonify(profile_add_on = user.profile_add_on,
#                      age = user.age,
#                      sex = user.gender,
#                      image = user.image,
#                      username = user.username,
#                      user_id = userid)

    return render_template('userprofile.html', user=user, filename = user.image)



@app.route('/profiles/', methods=['GET'])
def show_users():
  users = Profiles.query.all()
  user_list = {}
  user_list ['users'] = []
  if request.method == 'GET':# and request.headers['Content-Type'] == 'application/json':
    for u in users:
      tmp = {
        'username': u.username,
        'user_id': u.userid
      }
      user_list['users'].append(tmp)
    return jsonify(user_list)
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