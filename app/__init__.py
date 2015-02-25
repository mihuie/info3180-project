from flask import Flask
from flask.ext.sqlalchemy import SQLAlchemy


app = Flask(__name__)
# app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql://action@localhost/action'
app.config['SQLALCHEMY_DATABASE_URI'] = 'postgres://diosqsnmxxhrit:kRQOFycM4Xw_65etJEN3mh_fV9@ec2-50-17-202-29.compute-1.amazonaws.com:5432/de8p87fvfvr5o4'
app.secret_key = 'my superrr dupper secret_key'
db = SQLAlchemy(app)

from app import views, models





