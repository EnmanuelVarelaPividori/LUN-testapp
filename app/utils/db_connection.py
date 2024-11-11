from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()

def init_db(app):
    # Database configuration
    app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql://lun:password@localhost:5432/lun_db'  # Replace with environment variables for better security
    app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False  # Optional, disables a warning

    # Initialize SQLAlchemy with the app
    db.init_app(app)