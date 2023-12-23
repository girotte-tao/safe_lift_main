from app.models.base.base import BaseModel
from app.models.db import db

class UWB(BaseModel):
    name = db.Column(db.String(120), unique=False, nullable=False)
    position = db.Column(db.String(120), unique=False, nullable=False)
