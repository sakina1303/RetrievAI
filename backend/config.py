import os
from datetime import timedelta

class Config:
    # Secret Keys
    SECRET_KEY = os.environ.get('SECRET_KEY', 'your-secret-key-change-in-production')
    JWT_SECRET_KEY = os.environ.get('JWT_SECRET_KEY', 'jwt-secret-key-change-in-production')
    JWT_ACCESS_TOKEN_EXPIRES = timedelta(hours=24)
    
    # Database Configuration
    SQLALCHEMY_DATABASE_URI = os.environ.get(
        'DATABASE_URL', 
        'postgresql://localhost/lost_and_found_db'
    )
    SQLALCHEMY_TRACK_MODIFICATIONS = False
    
    # File Upload Configuration
    UPLOAD_FOLDER = os.path.join(os.path.dirname(os.path.abspath(__file__)), 'uploads')
    MAX_CONTENT_LENGTH = 16 * 1024 * 1024  # 16MB max file size
    ALLOWED_EXTENSIONS = {'png', 'jpg', 'jpeg', 'gif'}
    
    # AI API Configuration
    GEMINI_API_KEY = os.environ.get('GEMINI_API_KEY', '')
    OPENAI_API_KEY = os.environ.get('OPENAI_API_KEY', '')
    AI_PROVIDER = os.environ.get('AI_PROVIDER', 'gemini')  # 'gemini' or 'openai'
    
    # AI Matching Threshold
    SIMILARITY_THRESHOLD = 0.7  # 70% similarity threshold for matches
