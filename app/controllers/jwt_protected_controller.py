from flask import Blueprint, request, jsonify
from flask_jwt_extended import jwt_required
from app.services.jwt_protected_service import JWTProtectedService

jwt_protected_bp = Blueprint('jwt_protected', __name__)

@jwt_protected_bp.route('/data', methods=['GET', 'POST', 'PUT', 'DELETE'])
@jwt_required()
def handle_protected_data():
    if request.method == 'GET':
        data = JWTProtectedService.get_all_data()
        return jsonify(data), 200
    elif request.method == 'POST':
        new_data = request.json
        created_data = JWTProtectedService.create_data(new_data)
        return jsonify({"message": "Data created", "id": created_data.id}), 201
    elif request.method == 'PUT':
        data = request.json
        updated_data = JWTProtectedService.update_data(data)
        return jsonify({"message": "Data updated", "id": updated_data.id}), 200
    elif request.method == 'DELETE':
        data_id = request.args.get('id')
        JWTProtectedService.delete_data(data_id)
        return jsonify({"message": "Data deleted"}), 200