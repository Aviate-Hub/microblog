# Login form

from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, BooleanField, SubmitField, TextAreaField
from wtforms.validators import DataRequired, ValidationError, Email, EqualTo, Length
from app.models import User

# User login form
class LoginForm(FlaskForm):
    username = StringField('Username:', validators=[DataRequired()])
    password = PasswordField('Password:', validators=[DataRequired()])
    remember_me = BooleanField('Remember Me')
    submit = SubmitField('Sign In')


# User registration form
class RegistrationForm(FlaskForm):
    username = StringField('Username:', validators=[DataRequired()])
    email = StringField('Email:', validators=[DataRequired(), Email()])
    password = PasswordField('Password:', validators=[DataRequired()])
    password2 = PasswordField('Repeat Password:', validators=[DataRequired(), EqualTo('password')])
    submit = SubmitField('Register')

    # Check to see if username exists in DB
    def validate_username(self, username):
        user = User.query.filter_by(username=username.data).first()
        if user is not None:
            raise ValidationError('Please use a different username.')

    # Check to see if email exists in DB
    def validate_email(self, email):
        user = User.query.filter_by(email=email.data).first()
        if user is not None:
            raise ValidationError('Please use a different email address.')


# Profile editor form
class EditProfileForm(FlaskForm):
    username = StringField('Username:', validators=[DataRequired()])
    about_me = TextAreaField('About me:', validators=[Length(min=0, max=140)])
    submit = SubmitField('Submit')
