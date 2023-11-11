# описание метода в документации

import bcrypt
import dotenv
import random
import rethinkdb as r
# from rises import *
from flask import request
from flask_login import logout_user, LoginManager
from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, SubmitField
from wtforms.validators import InputRequired, Length, ValidationError
from flask import jsonify, request, send_file, session
rdb = r.RethinkDB()
conn = rdb.connect(host='localhost', port=28015)
dotenv.load_dotenv()

# login_manager = LoginManager(app)


# def hash_password(password):
#     salt = bcrypt.gensalt(13)
#     hash_password = bcrypt.hashpw(password.encode("UTF-8"), salt)
#     return hash_password
#
#
# def check_password(password, hashed_password):
#     return bcrypt.checkpw(password.encode("UTF-8"), hashed_password)


# class UserLogin:
#     def fromDB(self, user_id, db):
#         self.__user = db.getUser(user_id)
#         return self
#
#     def create(self, user):
#         self.__user = user
#         return self
#
#     def is_authenticated(self):
#         return True
#
#     def is_active(self):
#         return True
#
#     def is_anonymous(self):
#         return False
#
#     def get_id(self):
#         return str(self.__user['id'])
#
#
# @login_manager.user_loader
# def load_user(user_id):
#     print("load_user")
#     return UserLogin().fromDB(user_id, dbase)


# class RegisterForm(FlaskForm):
#     username = StringField(validators=[
#         InputRequired(), Length(min=4, max=20)], render_kw={"placeholder": "Username"})
#
#     password = PasswordField(validators=[
#         InputRequired(), Length(min=8, max=20)], render_kw={"placeholder": "Password"})
#
#     submit = SubmitField('Register')
#
#     def validate_username(self, username):
#         existing_user_username = User.query.filter_by(username=username.data).first()
#         if existing_user_username:
#             raise ValidationError(
#                 'That username already exists. Please choose a different one.')
#
#
# class LoginForm(FlaskForm):
#     username = StringField(validators=[
#         InputRequired(), Length(min=4, max=20)], render_kw={"placeholder": "Username"})
#
#     password = PasswordField(validators=[
#         InputRequired(), Length(min=8, max=20)], render_kw={"placeholder": "Password"})
#
#     submit = SubmitField('Login')

def get_post():
    book_ids = []
    posts = []

    books_info = rdb.db('meetingsBook').table('books').pluck("id").run(conn)
    for book_id in books_info:
        book_ids.append(book_id["id"])
    random_book_id = random.choice(book_ids)

    posts_info = list(rdb.db('meetingsBook').table('posts').filter({'book_id': random_book_id}).run(conn))
    for post in posts_info:
        posts.append(post)

    random_post = random.choice(posts)

    [author_name] = list(rdb.db('meetingsBook').table('authors').filter({'id': random_post['author_id']}).run(conn))
    [book_name] = list(rdb.db('meetingsBook').table('books').filter({'id': random_post['book_id']}).run(conn))

    return jsonify({'id':random_post['id'],"author_name": author_name['name'],"book_name":book_name['label'],'post':random_post['context']})
# def login():
#     message = ''
#     if request.method == 'POST':
#         print(request.form)
#         username = request.form.get('username')
#         password = request.form.get('password')
#         valid = bcrypt.checkpw(password.encode(), hashAndSalt)
#         if username == 'root' and password == 'pass':
#             message = "Correct username and password"
#         else:
#             message = "Wrong username or password"
#
#     return 1

#
# def logout():
#     logout_user()
#     return 1
#
#
# def register():
#     form = RegisterForm()
#     if form.validate_on_submit():
#         # password = userInput
#         # save "hashAndSalt" in data base
#
#         # new_user = User(username=form.username.data, password=hashed_password)
#         return 1
#
#     return 1
