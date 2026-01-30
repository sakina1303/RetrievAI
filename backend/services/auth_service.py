from repositories.user_repository import UserRepository
from flask_jwt_extended import create_access_token

class AuthService:
    @staticmethod
    def register_user(name, email, password, role='user'):
        """Register a new user"""
        # Check if user already exists
        existing_user = UserRepository.find_by_email(email)
        if existing_user:
            raise ValueError("User with this email already exists")
        
        # Create new user
        user = UserRepository.create(name, email, password, role)
        return user
    
    @staticmethod
    def login_user(email, password):
        """Authenticate user and return JWT token"""
        user = UserRepository.find_by_email(email)
        
        if not user or not user.check_password(password):
            raise ValueError("Invalid email or password")
        
        # Create JWT token with user data
        access_token = create_access_token(
            identity=user.id,
            additional_claims={
                'email': user.email,
                'name': user.name,
                'role': user.role
            }
        )
        
        return {
            'access_token': access_token,
            'user': user.to_dict()
        }
    
    @staticmethod
    def get_user_by_id(user_id):
        """Get user by ID"""
        return UserRepository.find_by_id(user_id)
