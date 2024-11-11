from flask import Flask
from flask_migrate import Migrate
from flask_jwt_extended import JWTManager
from flask_cors import CORS
from app.utils.db_connection import db, init_db  # Import the db instance and init function
from app.utils.blueprint_registry import register_blueprints

def create_app():
    app = Flask(__name__)

    # Enable CORS
    cors = CORS(app, resources={r"/api/*": {"origins": "http://localhost:3000"}})

    # Load secrets
    app.config['SECRET_KEY'] = 'your_secret_key'  # Replace with environment variable for security
    app.config['JWT_SECRET_KEY'] = 'your-secret-key'  # Replace with environment variable for security

    # Initialize JWT
    jwt = JWTManager(app)

    # Initialize the database
    init_db(app)  # Import and initialize the db configuration

    # Apply migrations
    migrate = Migrate(app, db)

    # Register blueprints
    register_blueprints(app)

    return app