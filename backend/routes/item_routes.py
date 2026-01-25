from flask import Blueprint, request, jsonify
from flask_jwt_extended import jwt_required, get_jwt_identity
from services.item_service import ItemService
from utils.file_utils import save_uploaded_file

item_bp = Blueprint('items', __name__)
item_service = ItemService()

@item_bp.route('/lost', methods=['POST'])
@jwt_required()
def create_lost_item():
    """Create a new lost item report"""
    try:
        user_id = get_jwt_identity()
        
        # Handle multipart/form-data
        name = request.form.get('name')
        description = request.form.get('description')
        location = request.form.get('location')
        image = request.files.get('image')
        
        if not name or not description or not location:
            return jsonify({'error': 'Name, description, and location are required'}), 400
        
        # Save image if provided
        image_filename = None
        if image:
            image_filename = save_uploaded_file(image)
        
        # Create lost item
        item = item_service.create_lost_item(name, description, image_filename, location, user_id)
        
        return jsonify({
            'message': 'Lost item reported successfully',
            'item': item.to_dict()
        }), 201
        
    except Exception as e:
        return jsonify({'error': 'Failed to create lost item', 'details': str(e)}), 500

@item_bp.route('/found', methods=['POST'])
@jwt_required()
def create_found_item():
    """Create a new found item report"""
    try:
        user_id = get_jwt_identity()
        
        # Handle multipart/form-data
        name = request.form.get('name')
        description = request.form.get('description')
        location = request.form.get('location')
        image = request.files.get('image')
        
        if not name or not description or not location:
            return jsonify({'error': 'Name, description, and location are required'}), 400
        
        # Save image if provided
        image_filename = None
        if image:
            image_filename = save_uploaded_file(image)
        
        # Create found item
        item = item_service.create_found_item(name, description, image_filename, location, user_id)
        
        return jsonify({
            'message': 'Found item reported successfully',
            'item': item.to_dict()
        }), 201
        
    except Exception as e:
        return jsonify({'error': 'Failed to create found item', 'details': str(e)}), 500

@item_bp.route('/lost', methods=['GET'])
@jwt_required()
def get_all_lost_items():
    """Get all lost items"""
    try:
        items = item_service.get_all_lost_items()
        return jsonify({
            'items': [item.to_dict() for item in items]
        }), 200
    except Exception as e:
        return jsonify({'error': 'Failed to get lost items', 'details': str(e)}), 500

@item_bp.route('/found', methods=['GET'])
@jwt_required()
def get_all_found_items():
    """Get all found items"""
    try:
        items = item_service.get_all_found_items()
        return jsonify({
            'items': [item.to_dict() for item in items]
        }), 200
    except Exception as e:
        return jsonify({'error': 'Failed to get found items', 'details': str(e)}), 500

@item_bp.route('/lost/<int:item_id>', methods=['GET'])
@jwt_required()
def get_lost_item(item_id):
    """Get lost item by ID"""
    try:
        item = item_service.get_lost_item(item_id)
        if not item:
            return jsonify({'error': 'Lost item not found'}), 404
        return jsonify({'item': item.to_dict()}), 200
    except Exception as e:
        return jsonify({'error': 'Failed to get lost item', 'details': str(e)}), 500

@item_bp.route('/found/<int:item_id>', methods=['GET'])
@jwt_required()
def get_found_item(item_id):
    """Get found item by ID"""
    try:
        item = item_service.get_found_item(item_id)
        if not item:
            return jsonify({'error': 'Found item not found'}), 404
        return jsonify({'item': item.to_dict()}), 200
    except Exception as e:
        return jsonify({'error': 'Failed to get found item', 'details': str(e)}), 500

@item_bp.route('/my-lost-items', methods=['GET'])
@jwt_required()
def get_my_lost_items():
    """Get current user's lost items"""
    try:
        user_id = get_jwt_identity()
        items = item_service.get_user_lost_items(user_id)
        return jsonify({
            'items': [item.to_dict() for item in items]
        }), 200
    except Exception as e:
        return jsonify({'error': 'Failed to get your lost items', 'details': str(e)}), 500

@item_bp.route('/my-found-items', methods=['GET'])
@jwt_required()
def get_my_found_items():
    """Get current user's found items"""
    try:
        user_id = get_jwt_identity()
        items = item_service.get_user_found_items(user_id)
        return jsonify({
            'items': [item.to_dict() for item in items]
        }), 200
    except Exception as e:
        return jsonify({'error': 'Failed to get your found items', 'details': str(e)}), 500

@item_bp.route('/lost/<int:item_id>/matches', methods=['GET'])
@jwt_required()
def get_matches_for_lost_item(item_id):
    """Get AI-powered matches for a lost item"""
    try:
        matches = item_service.find_matches_for_lost_item(item_id)
        return jsonify({
            'matches': matches
        }), 200
    except ValueError as e:
        return jsonify({'error': str(e)}), 404
    except Exception as e:
        return jsonify({'error': 'Failed to find matches', 'details': str(e)}), 500

@item_bp.route('/found/<int:item_id>/matches', methods=['GET'])
@jwt_required()
def get_matches_for_found_item(item_id):
    """Get AI-powered matches for a found item"""
    try:
        matches = item_service.find_matches_for_found_item(item_id)
        return jsonify({
            'matches': matches
        }), 200
    except ValueError as e:
        return jsonify({'error': str(e)}), 404
    except Exception as e:
        return jsonify({'error': 'Failed to find matches', 'details': str(e)}), 500

@item_bp.route('/lost/<int:item_id>', methods=['DELETE'])
@jwt_required()
def delete_lost_item(item_id):
    """Delete a lost item"""
    try:
        user_id = get_jwt_identity()
        item_service.delete_lost_item(item_id, user_id)
        return jsonify({'message': 'Lost item deleted successfully'}), 200
    except ValueError as e:
        return jsonify({'error': str(e)}), 404
    except PermissionError as e:
        return jsonify({'error': str(e)}), 403
    except Exception as e:
        return jsonify({'error': 'Failed to delete lost item', 'details': str(e)}), 500

@item_bp.route('/found/<int:item_id>', methods=['DELETE'])
@jwt_required()
def delete_found_item(item_id):
    """Delete a found item"""
    try:
        user_id = get_jwt_identity()
        item_service.delete_found_item(item_id, user_id)
        return jsonify({'message': 'Found item deleted successfully'}), 200
    except ValueError as e:
        return jsonify({'error': str(e)}), 404
    except PermissionError as e:
        return jsonify({'error': str(e)}), 403
    except Exception as e:
        return jsonify({'error': 'Failed to delete found item', 'details': str(e)}), 500
