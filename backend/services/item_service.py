from repositories.item_repository import ItemRepository
from services.ai_match_service import AIMatchService

class ItemService:
    def __init__(self):
        self.ai_service = AIMatchService()
    
    def create_lost_item(self, name, description, image, location, user_id):
        """Create a new lost item report"""
        item = ItemRepository.create_lost_item(name, description, image, location, user_id)
        return item
    
    def create_found_item(self, name, description, image, location, user_id):
        """Create a new found item report"""
        item = ItemRepository.create_found_item(name, description, image, location, user_id)
        return item
    
    def get_all_lost_items(self):
        """Get all lost items"""
        return ItemRepository.get_all_lost_items()
    
    def get_all_found_items(self):
        """Get all found items"""
        return ItemRepository.get_all_found_items()
    
    def get_lost_item(self, item_id):
        """Get lost item by ID"""
        return ItemRepository.get_lost_item_by_id(item_id)
    
    def get_found_item(self, item_id):
        """Get found item by ID"""
        return ItemRepository.get_found_item_by_id(item_id)
    
    def get_user_lost_items(self, user_id):
        """Get all lost items reported by a user"""
        return ItemRepository.get_user_lost_items(user_id)
    
    def get_user_found_items(self, user_id):
        """Get all found items reported by a user"""
        return ItemRepository.get_user_found_items(user_id)
    
    def find_matches_for_lost_item(self, lost_item_id):
        """Find matching found items for a lost item using AI"""
        lost_item = ItemRepository.get_lost_item_by_id(lost_item_id)
        if not lost_item:
            raise ValueError("Lost item not found")
        
        found_items = ItemRepository.get_all_found_items()
        matches = self.ai_service.find_matches_for_lost_item(lost_item, found_items)
        
        return matches
    
    def find_matches_for_found_item(self, found_item_id):
        """Find matching lost items for a found item using AI"""
        found_item = ItemRepository.get_found_item_by_id(found_item_id)
        if not found_item:
            raise ValueError("Found item not found")
        
        lost_items = ItemRepository.get_all_lost_items()
        matches = self.ai_service.find_matches_for_found_item(found_item, lost_items)
        
        return matches
    
    def update_lost_item_status(self, item_id, status):
        """Update lost item status"""
        return ItemRepository.update_lost_item_status(item_id, status)
    
    def update_found_item_status(self, item_id, status):
        """Update found item status"""
        return ItemRepository.update_found_item_status(item_id, status)
    
    def delete_lost_item(self, item_id, user_id):
        """Delete a lost item (only by owner or admin)"""
        item = ItemRepository.get_lost_item_by_id(item_id)
        if not item:
            raise ValueError("Lost item not found")
        
        if item.user_id != user_id:
            raise PermissionError("You can only delete your own items")
        
        return ItemRepository.delete_lost_item(item_id)
    
    def delete_found_item(self, item_id, user_id):
        """Delete a found item (only by owner or admin)"""
        item = ItemRepository.get_found_item_by_id(item_id)
        if not item:
            raise ValueError("Found item not found")
        
        if item.user_id != user_id:
            raise PermissionError("You can only delete your own items")
        
        return ItemRepository.delete_found_item(item_id)
