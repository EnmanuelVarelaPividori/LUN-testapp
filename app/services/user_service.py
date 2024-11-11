from app.models.user_model import User
from app.utils.db_connection import db
from werkzeug.security import generate_password_hash

class UserService:
    @staticmethod
    def create_user(username, password):
        hashed_password = generate_password_hash(password)
        user = User(username=username, password=hashed_password)
        db.session.add(user)
        db.session.commit()
        return user

    @staticmethod
    def get_user_by_username(username):
        return User.query.filter_by(username=username).first()