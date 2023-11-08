from flask import Blueprint, request
from app.handlers.towerCraneHandler import *

api = Blueprint('tower_crane_api', __name__)

@api.route('/towercrane/<tower_crane_id>', methods=['GET'])
def get_tower_crane_by_id(tower_crane_id):
    # 处理获取用户信息的逻辑
    return get_tower_crane_by_id(tower_crane_id)

@api.route('/towercrane', methods=['GET'])
def get_tower_crane():
    # 处理获取用户信息的逻辑
    return 'tower_crane'

@api.route('/towercrane', methods=['POST'])
def create_tower_crane():
    data = request.get_json()
    name = data.get('name')
    position = data.get('position')
    res = creat_tower_crane(name, position)

    return res