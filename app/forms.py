from flask.ext.wtf import Form
from wtforms.fields import StringField, IntegerField, SubmitField, FileField, SelectField
from wtforms.validators import Required, Length, NumberRange
from flask_wtf.file import FileField


class CreateUserForm(Form):
    username = StringField('Username', validators=[Length(min=4, max=25)])
    firstname = StringField('First Name', validators=[Length(min=4, max=25)])
    lastname = StringField('Last Name', validators=[Length(min=2, max=25)])
    age = IntegerField('Age', validators=[NumberRange(min=16, max=99)])
    gender = SelectField('Gender', choices=[('male', 'Male'), ('Female','Female')])    
    image = FileField('Image File', validators=[Required()])
    submit = SubmitField("Register")