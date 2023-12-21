from flask import Blueprint

api = Blueprint('hello_api', __name__)

@api.route('/api/hello')
def about():
    return 'hello'