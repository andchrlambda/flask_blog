from flask_wtf import FlaskForm
from flask_wtf.file import FileField, FileAllowed
from flask_login import current_user
from wtforms import StringField, PasswordField, SubmitField, BooleanField
from wtforms.validators import DataRequired, Length, Email, EqualTo, ValidationError
from flaskblog.models import User

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

    def validate_username(self, username):
        """A function to check whether username already exists in database
        If user = none, it will be accepted; otherwise the conditional activates the
        validation error.
        """
        user = User.query.filter_by(username=username.data).first()
        if user:
            raise ValidationError('That username is taken. Please choose another.')

    def validate_email(self, email):
        """A function to check whether email already exists in database
        If email = none, it will be accepted, otherwise the conditional activates the
        validation error.
        """
        user = User.query.filter_by(email=email.data).first()
        if user:
            raise ValidationError('That email is taken. Please choose a different one.')
  
    
    """
    def validate_field(self, field):
        'A general function to validate registration fields'
        if True:
            raise ValidationError('Validation Message')
    """    

class LoginForm(FlaskForm):
    email = StringField('Email',
                validators=[DataRequired(), Email()])
    password = PasswordField('Password', validators=[DataRequired()])
    remember = BooleanField('Remember me')
    """remember uses a cookie to allow users to stay logged in; required Boolean field"""     
    submit = SubmitField('Log in')    

class UpdateAccountForm(FlaskForm):
    """Inherits from FlaskForm"""
    username = StringField('Username', 
                validators=[DataRequired(), Length(min=2, max=20)])
    """Validators are classes that we import"""
    email = StringField('Email',
                validators=[DataRequired(), Email()])
    picture = FileField('Update Profile Picture', validators=[FileAllowed(['jpg', 'png'])])
    submit = SubmitField('Update')   

    def validate_username(self, username):
        """A function to check whether username already exists in database
        If user = none, it will be accepted; otherwise the conditional activates the
        validation error.
        """
        if username.data != current_user.username:
            user = User.query.filter_by(username=username.data).first()
            if user:
                raise ValidationError('That username is taken. Please choose another.')

    def validate_email(self, email):
        """A function to check whether email already exists in database
        If email = none, it will be accepted, otherwise the conditional activates the
        validation error.
        """
        if email.data != current_user.email:
            user = User.query.filter_by(email=email.data).first()
            if user:
                raise ValidationError('That email is taken. Please choose a different one.') 