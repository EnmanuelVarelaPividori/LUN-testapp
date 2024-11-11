from flask import Blueprint, request, jsonify
from flask_jwt_extended import create_access_token
from app.services.user_service import UserService

user_bp = Blueprint('user', __name__)

@user_bp.route('/test', methods=['GET'])
def test_route():
    return jsonify({"message": "Test route is working"}), 200

@user_bp.route('/register', methods=['POST'])
def register_user():
    data = request.json
    username = data.get('username')
    password = data.get('password')

    if not username or not password:
        return jsonify({"error": "Username and password are required"}), 400

    try:
        user = UserService.create_user(username, password)
        return jsonify({"message": "User created", "user_id": user.id}), 201
    except Exception as e:
        return jsonify({"error": str(e)}), 500

@user_bp.route('/login', methods=['POST'])
def login_user():
    data = request.json
    username = data.get('username')
    password = data.get('password')

    if not username or not password:
        return jsonify({"error": "Username and password are required"}), 400

    user = UserService.get_user_by_username(username)
    if not user or not user.check_password(password):
        return jsonify({"error": "Invalid username or password"}), 401

    # Create JWT token
    access_token = create_access_token(identity={'id': user.id, 'username': user.username})
    return jsonify({"access_token": access_token}), 200