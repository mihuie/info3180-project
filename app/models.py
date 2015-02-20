from . import db

class Profiles(db.Model):
    userid = db.Column(db.String(30), primary_key=True)
    username = db.Column(db.String(30), unique=True)
    firstname = db.Column(db.String(30), unique=False)
    lastname = db.Column(db.String(30), unique=False)
    age = db.Column(db.Integer, unique=False)
    gender = db.Column(db.String(10), unique=False)
    datecreated = db.Column(db.String(20), unique=False)
    
    
    def __init__(self, userid, username, firstname, lastname, age, gender, datecreated):
        self.userid = userid
        self.username = username
        self.firstname = firstname
        self.lastname = lastname
        self.age = age
        self.gender = gender
        self.datecreated = datecreated
      

    def __repr__(self):
        return '<Profiles %r>' % self.username