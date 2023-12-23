import json


def handle_uwb_status(message, uwb_manager):
    try:
        data = json.loads(message)
        return uwb_manager.update_status(data["TAG-ID"], data["status"])

    except (ValueError, KeyError) as e:
        print("Error processing UWB message:", e)
