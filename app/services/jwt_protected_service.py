from app.models.jwt_protected_model import JWTProtectedData
from app.utils.db_connection import db

class JWTProtectedService:
    @staticmethod
    def get_all_data():
        return JWTProtectedData.query.all()

    @staticmethod
    def create_data(data):
        new_data = JWTProtectedData(**data)
        db.session.add(new_data)
        db.session.commit()
        return new_data

    @staticmethod
    def update_data(data):
        existing_data = JWTProtectedData.query.get(data['id'])
        if not existing_data:
            raise Exception("Data not found")

        for key, value in data.items():
            if hasattr(existing_data, key):
                setattr(existing_data, key, value)

        db.session.commit()
        return existing_data

    @staticmethod
    def delete_data(data_id):
        data = JWTProtectedData.query.get(data_id)
        if not data:
            raise Exception("Data not found")

        db.session.delete(data)
        db.session.commit()