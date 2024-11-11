from app.models.open_model import OpenData
from app.utils.db_connection import db

class OpenRepository:
    def get_all_data(self):
        return OpenData.query.all()

    def create_data(self, data):
        new_data = OpenData(**data)
        db.session.add(new_data)
        db.session.commit()
        return new_data

    def get_data_by_id(self, data_id):
        return OpenData.query.get(data_id)

    def update_data(self, data):
        existing_data = self.get_data_by_id(data['id'])
        if not existing_data:
            raise Exception("Data not found")

        for key, value in data.items():
            if hasattr(existing_data, key):
                setattr(existing_data, key, value)

        db.session.commit()
        return existing_data

    def delete_data(self, data_id):
        data = self.get_data_by_id(data_id)
        if not data:
            raise Exception("Data not found")

        db.session.delete(data)
        db.session.commit()