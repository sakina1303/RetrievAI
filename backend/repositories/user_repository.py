from models import User
from database import db

class UserRepository:
    @staticmethod
    def create(name, email, password, role='user'):
        user = User(name=name, email=email, role=role)
        user.set_password(password)
        db.session.add(user)
        db.session.commit()
        return user
    
    @staticmethod
    def find_by_email(email):
        return User.query.filter_by(email=email).first()
    
    @staticmethod
    def find_by_id(user_id):
        return User.query.get(user_id)
    
    @staticmethod
    def get_all():
        return User.query.all()
    
    @staticmethod
    def delete(user_id):
        user = User.query.get(user_id)
        if user:
            db.session.delete(user)
            db.session.commit()
            return True
        return False
