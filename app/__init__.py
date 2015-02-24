from flask import Flask
from flask.ext.sqlalchemy import SQLAlchemy
import logging
import sys

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql://action@localhost/action'

db = SQLAlchemy(app)
app.logger.addHandler(logging.StreamHandler(sys.stdout))
app.logger.setLevel(logging.ERROR)

from app import views, models
from app.models import Profiles
from app import db


db.create_all()
