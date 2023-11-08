from app import db

class TowerCrane(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(120), unique=True, nullable=False)
    position = db.Column(db.String(120), unique=True, nullable=False)