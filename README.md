
# Safe Lift Main

## Overview
This Flask application is designed to handle and process hardware data, managing hardware status, and communicating with the frontend using Flask-SocketIO. It's deployed using Eventlet and recommended to be run in a Docker container.

## Prerequisites
- Python 3.x

## Usage

Once the application is running, it will start accepting hardware data, processing it, and managing the hardware status. Real-time updates are sent to the connected frontend clients using Flask-SocketIO.

## Development

To run the application locally without Docker:

1. **Install Dependencies:**
   ```bash
   pip install -r requirements.txt
   ```

2. **Run the Application:**
   ```bash
   python app.py
   ```

   This will start the server on `localhost:8000`.


## Acknowledgments

- todo
