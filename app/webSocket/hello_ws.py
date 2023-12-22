from flask_socketio import SocketIO, emit

def setup_socketio(app):
    socketio = SocketIO(app, cors_allowed_origins="*")

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

    return socketio
