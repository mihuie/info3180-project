from . import db

class Profiles(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    userid = db.Column(db.String, unique=True)
    username = db.Column(db.String(30), unique=True)
    firstname = db.Column(db.String(30), unique=False)
    lastname = db.Column(db.String(30), unique=False)
    age = db.Column(db.Integer, unique=False)
    gender = db.Column(db.String(10), unique=False)
    date_created = db.Column(db.String(15), unique=False)
    
    def __init__(self, userid, username, firstname, lastname, age, gender, date_created):
        self.userid = userid
        self.username = username
        self.firstname = firstname
        self.lastname = lastname
        self.age = age
        self.gender = gender
        self.date_created = date_created

    def __repr__(self):
        return '<User %r>' % self.username