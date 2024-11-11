def register_blueprints(app):
    from app.controllers.user_controller import user_bp
    from app.controllers.jwt_protected_controller import jwt_protected_bp
    from app.controllers.open_controller import open_bp

    app.register_blueprint(user_bp, url_prefix='/api/users')
    print("User blueprint registered")
    app.register_blueprint(jwt_protected_bp, url_prefix='/api/protected')
    app.register_blueprint(open_bp, url_prefix='/api/open')