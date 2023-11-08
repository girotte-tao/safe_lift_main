from datetime import datetime
from app.models.base.base import BaseModel

from app.models.db import db


class TowerCraneStatus(BaseModel):
    tower_crane_id = db.Column(db.Integer, db.ForeignKey('tower_crane.id'), nullable=False)
    status_code = db.Column(db.Integer, nullable=False)
    status = db.Column(db.String(120), unique=True, nullable=False)
    log_time = db.Column(db.DateTime, default=datetime.utcnow)
