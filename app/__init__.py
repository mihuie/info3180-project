from flask import Flask
from flask.ext.sqlalchemy import SQLAlchemy
import logging
# import sys
from app import views, models

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql://action@localhost/action'

db = SQLAlchemy(app)
# app.logger.addHandler(logging.StreamHandler(sys.stdout))
# app.logger.setLevel(logging.ERROR)



