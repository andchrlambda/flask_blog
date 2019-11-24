from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, SubmitField, BooleanField
from wtforms.validators import DataRequired, Length, Email, EqualTo

"""
Writing Python classes that represent forms.
"""

class RegistrationForm(FlaskForm):
    """Inherits from FlaskForm"""
    username = StringField('Username', 
                validators=[DataRequired(), Length(min=2, max=20)])
    """Validators are classes that we import"""
    email = StringField('Email',
                validators=[DataRequired(), Email()])
    password = PasswordField('Password', validators=[DataRequired()])    
    confirm_password = PasswordField('Confirm Password', 
                                    validators=[DataRequired(), EqualTo('password')])   

    submit = SubmitField('Sign Up')

class LoginForm(FlaskForm):
    email = StringField('Email',
                validators=[DataRequired(), Email()])
    password = PasswordField('Password', validators=[DataRequired()])
    remember = BooleanField('Remember me')
    """remember uses a cookie to allow users to stay logged in; required Boolean field"""     
    submit = SubmitField('Log in')    