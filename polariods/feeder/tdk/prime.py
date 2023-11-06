# описание метода в документации

import bcrypt
import dotenv
from rises import *
from flask import request
from flask_login import logout_user, LoginManager
from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, SubmitField
from wtforms.validators import InputRequired, Length, ValidationError

dotenv.load_dotenv()

login_manager = LoginManager(app)


def hash_password(password):
    salt = bcrypt.gensalt(13)
    hash_password = bcrypt.hashpw(password.encode("UTF-8"), salt)
    return hash_password


def check_password(password, hashed_password):
    return bcrypt.checkpw(password.encode("UTF-8"), hashed_password)


class UserLogin:
    def fromDB(self, user_id, db):
        self.__user = db.getUser(user_id)
        return self

    def create(self, user):
        self.__user = user
        return self

    def is_authenticated(self):
        return True

    def is_active(self):
        return True

    def is_anonymous(self):
        return False

    def get_id(self):
        return str(self.__user['id'])


@login_manager.user_loader
def load_user(user_id):
    print("load_user")
    return UserLogin().fromDB(user_id, dbase)


class RegisterForm(FlaskForm):
    username = StringField(validators=[
        InputRequired(), Length(min=4, max=20)], render_kw={"placeholder": "Username"})

    password = PasswordField(validators=[
        InputRequired(), Length(min=8, max=20)], render_kw={"placeholder": "Password"})

    submit = SubmitField('Register')

    def validate_username(self, username):
        existing_user_username = User.query.filter_by(username=username.data).first()
        if existing_user_username:
            raise ValidationError(
                'That username already exists. Please choose a different one.')


class LoginForm(FlaskForm):
    username = StringField(validators=[
        InputRequired(), Length(min=4, max=20)], render_kw={"placeholder": "Username"})

    password = PasswordField(validators=[
        InputRequired(), Length(min=8, max=20)], render_kw={"placeholder": "Password"})

    submit = SubmitField('Login')


def login():
    message = ''
    if request.method == 'POST':
        print(request.form)
        username = request.form.get('username')
        password = request.form.get('password')
        valid = bcrypt.checkpw(password.encode(), hashAndSalt)
        if username == 'root' and password == 'pass':
            message = "Correct username and password"
        else:
            message = "Wrong username or password"

    return 1


def logout():
    logout_user()
    return 1


def register():
    form = RegisterForm()
    if form.validate_on_submit():
        # password = userInput
        # save "hashAndSalt" in data base

        # new_user = User(username=form.username.data, password=hashed_password)
        return 1

    return 1
