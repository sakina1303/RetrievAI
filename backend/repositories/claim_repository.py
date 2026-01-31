from models import Claim
from database import db

class ClaimRepository:
    @staticmethod
    def create(lost_item_id, found_item_id, claimant_user_id):
        claim = Claim(
            lost_item_id=lost_item_id,
            found_item_id=found_item_id,
            claimant_user_id=claimant_user_id
        )
        db.session.add(claim)
        db.session.commit()
        return claim
    
    @staticmethod
    def get_by_id(claim_id):
        return Claim.query.get(claim_id)
    
    @staticmethod
    def get_all():
        return Claim.query.order_by(Claim.created_at.desc()).all()
    
    @staticmethod
    def get_by_user(user_id):
        return Claim.query.filter_by(claimant_user_id=user_id).order_by(Claim.created_at.desc()).all()
    
    @staticmethod
    def get_pending_claims():
        return Claim.query.filter_by(status='pending').order_by(Claim.created_at.desc()).all()
    
    @staticmethod
    def update_status(claim_id, status):
        claim = Claim.query.get(claim_id)
        if claim:
            claim.status = status
            db.session.commit()
            return claim
        return None
    
    @staticmethod
    def delete(claim_id):
        claim = Claim.query.get(claim_id)
        if claim:
            db.session.delete(claim)
            db.session.commit()
            return True
        return False
    
    @staticmethod
    def check_existing_claim(lost_item_id, found_item_id, user_id):
        return Claim.query.filter_by(
            lost_item_id=lost_item_id,
            found_item_id=found_item_id,
            claimant_user_id=user_id
        ).first()
