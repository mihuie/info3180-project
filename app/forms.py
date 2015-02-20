from flask.ext.wtf import Form
from wtforms.fields import TextField
from wtforms.validators import Required
from werkzeug import secure_filename


class EmailPasswordForm(Form):
    username = TextField('Username', validators=[Required()])
    email = TextField('Email', validators=[Required(), Email()])