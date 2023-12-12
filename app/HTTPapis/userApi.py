from flask import Blueprint

api = Blueprint('user_api', __name__)

@api.route('/about')
def about():
    return 'About us'