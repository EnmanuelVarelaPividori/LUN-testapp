from app import db
from sqlalchemy.dialects.postgresql import JSON

class OpenData(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(100), nullable=False)
    value = db.Column(db.Float, nullable=False)
    meta_data = db.Column(JSON, nullable=True)