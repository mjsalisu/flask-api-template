from flask import Blueprint, request
from app.user.models import User

user = Blueprint('user', __name__, url_prefix='/user')

@user.post('create')
def create_user():
    name = request.json.get('name')
    username = request.json.get('username')
    password = request.json.get('password')

    user = User.get_by_username(username)
    if user:
        return 'Username with \'{}\' already exists.'.format(username), 400

    if name and username and password:
        User.create(name, username, password)
        return '{} account created for successfully.'.format(name), 200
    return 'Account creation failed, please try again', 400


@user.post('login')
def user_login():
    username = request.json.get('username')
    password = request.json.get('password')

    user = User.get_by_username(username)
    if user and user.check_password(password):
        return 'User logged in succcessful', 200
    return 'Invalid username or password', 400
