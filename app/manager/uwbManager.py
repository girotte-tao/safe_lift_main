import json


class UWBManager:
    def __init__(self, emit_function):
        self.uwb_status = {}
        self.emit = emit_function

    def update_status(self, tag_id, status):
        # 如果状态有更新，则更新该UWB的状态，返回当前所有状态，否则返回False
        if tag_id not in self.uwb_status or self.uwb_status[tag_id] != status:
            self.uwb_status[tag_id] = status
            print(f"Updated TAG-ID {tag_id} status to {status}")
            # self.emit('uwb', json.dumps(self.get_all_statuses()))
            return self.get_all_statuses()
        else:
            return False


    def get_status(self, tag_id):
        # 获取特定UWB的状态
        return self.uwb_status.get(tag_id, "Unknown")

    def get_all_statuses(self):
        # 返回所有UWB的状态列表，每个元素是一个包含tag_id和status的字典
        return [{"tag_id": tag_id, "status": status} for tag_id, status in self.uwb_status.items()]