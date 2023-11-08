from app.models.towerCrane import TowerCrane

from flask import jsonify


def creat_tower_crane(name, position):
    new_crane = TowerCrane(name=name, position=position)
    res = new_crane.save()
    return jsonify(res)


def get_tower_crane_by_id(tower_crane_id):
    TowerCrane.get_by_id(tower_crane_id)
