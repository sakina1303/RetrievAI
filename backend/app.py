from flask import Flask
from flask_cors import CORS
from flask_jwt_extended import JWTManager
from config import Config
from database import db
from routes.auth_routes import auth_bp
from routes.item_routes import item_bp
from routes.claim_routes import claim_bp
from routes.admin_routes import admin_bp

def create_app():
    app = Flask(__name__)
    app.config.from_object(Config)
    
    # Initialize extensions
    CORS(app)
    db.init_app(app)
    JWTManager(app)
    
    # Register blueprints
    app.register_blueprint(auth_bp, url_prefix='/api/auth')
    app.register_blueprint(item_bp, url_prefix='/api/items')
    app.register_blueprint(claim_bp, url_prefix='/api/claims')
    app.register_blueprint(admin_bp, url_prefix='/api/admin')
    
    # Create tables
    with app.app_context():
        db.create_all()
    
    @app.route('/')
    def health_check():
        return {'status': 'OK', 'message': 'AI Lost & Found API is running'}
    
    return app

if __name__ == '__main__':
    app = create_app()
    app.run(debug=True, host='0.0.0.0', port=5000)
