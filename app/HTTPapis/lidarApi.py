from flask import Blueprint, request
from app.handlers.towerCraneHandler import *
from app import socketio

api = Blueprint('lidar_api', __name__)


@api.route('/api/lidar_message', methods=['POST'])
def get_lidar_data():
    data = request.get_json()
    lidar_data = data.get('data')
    socketio.emit('lidar', lidar_data, namespace='/ws')
    return lidar_data