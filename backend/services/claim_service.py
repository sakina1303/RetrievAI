from repositories.claim_repository import ClaimRepository
from repositories.item_repository import ItemRepository

class ClaimService:
    @staticmethod
    def create_claim(lost_item_id, found_item_id, claimant_user_id):
        """Create a new claim request"""
        # Verify items exist
        lost_item = ItemRepository.get_lost_item_by_id(lost_item_id)
        found_item = ItemRepository.get_found_item_by_id(found_item_id)
        
        if not lost_item:
            raise ValueError("Lost item not found")
        if not found_item:
            raise ValueError("Found item not found")
        
        # Check if claim already exists
        existing_claim = ClaimRepository.check_existing_claim(
            lost_item_id, found_item_id, claimant_user_id
        )
        if existing_claim:
            raise ValueError("You have already submitted a claim for this item")
        
        # Create claim
        claim = ClaimRepository.create(lost_item_id, found_item_id, claimant_user_id)
        return claim
    
    @staticmethod
    def get_claim_by_id(claim_id):
        """Get claim by ID"""
        return ClaimRepository.get_by_id(claim_id)
    
    @staticmethod
    def get_all_claims():
        """Get all claims (admin only)"""
        return ClaimRepository.get_all()
    
    @staticmethod
    def get_user_claims(user_id):
        """Get all claims by a user"""
        return ClaimRepository.get_by_user(user_id)
    
    @staticmethod
    def get_pending_claims():
        """Get all pending claims (admin only)"""
        return ClaimRepository.get_pending_claims()
    
    @staticmethod
    def approve_claim(claim_id):
        """Approve a claim (admin only)"""
        claim = ClaimRepository.get_by_id(claim_id)
        if not claim:
            raise ValueError("Claim not found")
        
        if claim.status != 'pending':
            raise ValueError("Only pending claims can be approved")
        
        # Update claim status
        claim = ClaimRepository.update_status(claim_id, 'approved')
        
        # Update item statuses
        ItemRepository.update_lost_item_status(claim.lost_item_id, 'claimed')
        ItemRepository.update_found_item_status(claim.found_item_id, 'claimed')
        
        return claim
    
    @staticmethod
    def reject_claim(claim_id):
        """Reject a claim (admin only)"""
        claim = ClaimRepository.get_by_id(claim_id)
        if not claim:
            raise ValueError("Claim not found")
        
        if claim.status != 'pending':
            raise ValueError("Only pending claims can be rejected")
        
        # Update claim status
        claim = ClaimRepository.update_status(claim_id, 'rejected')
        return claim
    
    @staticmethod
    def delete_claim(claim_id):
        """Delete a claim"""
        return ClaimRepository.delete(claim_id)
