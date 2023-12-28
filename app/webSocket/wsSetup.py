import json

from flask_socketio import SocketIO, emit

from app.manager.uwbManager import UWBManager
from app.webSocket.uwbHandler import handle_uwb_status
from app.webSocket.lidar_handler import handle_lidar_message


def setup_socketio(app):
    socketio = SocketIO(app, cors_allowed_origins="*")
    uwb_manager = UWBManager(socketio.emit)

    @socketio.on('connect', namespace='/ws')
    def handle_connect():
        print('Client connected')

    @socketio.on('disconnect', namespace='/ws')
    def handle_disconnect():
        print('Client disconnected')

    @socketio.on('message', namespace='/ws')
    def handle_message(message):
        emit('message', 'Message received!: ' + message, namespace='/ws')

        all_status = handle_uwb_status(message, uwb_manager)
        if all_status:
            print('emit all_status', all_status)
            emit('uwb', json.dumps(all_status), broadcast=True)

    @socketio.on('uwb', namespace='/ws')
    def response_uwb_message(message):
        emit('uwb', 'Message received!: ' + message, namespace='/ws')

    @socketio.on('uwb_message', namespace='/ws')
    def handle_message(message):
        emit('uwb_message', 'Message received!: ' + message, namespace='/ws')

        all_status = handle_uwb_status(message, uwb_manager)
        if all_status:
            print('emit all_status', all_status)
            emit('uwb', json.dumps(all_status), broadcast=True)

    @socketio.on('lidar_message', namespace='/ws')
    def response_message(message):
        emit('lidar_message', 'lidar message received!: ' + message, namespace='/ws')

        lidar_message = handle_lidar_message(message)
        if lidar_message:
            emit('lidar', json.dumps(lidar_message), broadcast=True)

    @socketio.on('lidar', namespace='/ws')
    def response_lidar_message(message):
        emit('lidar', 'Message received!: ' + message, namespace='/ws')



    return socketio
