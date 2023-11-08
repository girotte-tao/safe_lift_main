from flask import Blueprint

api = Blueprint('hello_api', __name__)

@api.route('/')
def about():
    return 'hello'