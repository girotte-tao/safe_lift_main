from app.models.base.base import BaseModel
from app.models.db import db

class User(BaseModel):
    name = db.Column(db.String(120), unique=True, nullable=False)
    position = db.Column(db.String(120), unique=True, nullable=False)
