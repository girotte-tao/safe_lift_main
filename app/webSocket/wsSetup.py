import json

from flask_socketio import SocketIO, emit

from app.manager.uwbManager import UWBManager
from app.webSocket.uwbHandler import handle_uwb_status


def setup_socketio(app):
    socketio = SocketIO(app, cors_allowed_origins="*")
    uwb_manager = UWBManager(socketio.emit)

    @socketio.on('connect')
    def handle_connect():
        print('Client connected')

    @socketio.on('disconnect')
    def handle_disconnect():
        print('Client disconnected')

    @socketio.on('message')
    def handle_message(message):
        print('Received message:', message)
        emit('message', 'Message received!: ' + message)
        print('emit to uwb')
        # emit('uwb', 'Message received!: ' + 'uwb', broadcast=True)
        # emit('uwb', 'Message received!: ' + message, namespace='/uwb')

        all_status = handle_uwb_status(message, uwb_manager)
        if all_status:
            print('emit all_status', all_status)
            emit('uwb', json.dumps(all_status), broadcast=True)

    # @socketio.on('uwb', namespace='/uwb')
    @socketio.on('uwb')
    def handle_uwb_message(message):
        print('uwb'+message)
        print('Received message:', message)
        emit('uwb', 'Message received!: ' + message)

    return socketio
