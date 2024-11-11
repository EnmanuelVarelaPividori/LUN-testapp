from app import db
import datetime
from sqlalchemy.dialects.postgresql import JSON

class JWTProtectedData(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    data = db.Column(db.String(200), nullable=False)
    created_at = db.Column(db.Date, default=datetime.datetime.utcnow)
    additional_info = db.Column(JSON, nullable=False)  # JSON not customizable
    details = db.Column(JSON, nullable=True)  # JSON customizable
    is_active = db.Column(db.Boolean, default=True)