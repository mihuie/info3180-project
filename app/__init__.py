from flask import Flask
from flask.ext.sqlalchemy import SQLAlchemy
from app import views, models

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql://action@localhost/action'

db = SQLAlchemy(app)
db.create_all()

import logging
import sys
app.logger.addHandler(logging.StreamHandler(sys.stdout))
app.logger.setLevel(logging.ERROR)



