from flask import Blueprint, request, jsonify
from app.services.open_service import OpenService

open_bp = Blueprint('open', __name__)

@open_bp.route('/open-data', methods=['GET', 'POST', 'PUT', 'DELETE'])
def handle_open_data():
    if request.method == 'GET':
        data = OpenService.get_all_data()
        return jsonify(data), 200
    elif request.method == 'POST':
        new_data = request.json
        created_data = OpenService.create_data(new_data)
        return jsonify({"message": "Data created", "id": created_data.id}), 201
    elif request.method == 'PUT':
        data = request.json
        updated_data = OpenService.update_data(data)
        return jsonify({"message": "Data updated", "id": updated_data.id}), 200
    elif request.method == 'DELETE':
        data_id = request.args.get('id')
        OpenService.delete_data(data_id)
        return jsonify({"message": "Data deleted"}), 200