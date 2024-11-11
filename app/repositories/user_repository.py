from app.models.user_model import User
from app.utils.db_connection import db

class UserRepository:
    def create_user(self, username, password):
        user = User(username=username, password=password)
        db.session.add(user)
        db.session.commit()
        return user

    def get_user_by_username(self, username):
        return User.query.filter_by(username=username).first()