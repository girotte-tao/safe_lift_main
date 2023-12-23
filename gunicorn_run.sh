#gunicorn -k geventwebsocket.gunicorn.workers.GeventWebSocketWorker -w 1 -c gunicorn_config.py app:app
gunicorn -k geventwebsocket.gunicorn.workers.GeventWebSocketWorker -w 1 -c gunicorn_config.py -b 0.0.0.0:8000 app:app
