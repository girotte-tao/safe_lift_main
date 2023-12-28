import json


def handle_lidar_message(message):
    lidar_data = json.loads(message)
    return lidar_data
