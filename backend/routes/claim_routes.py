from flask import Blueprint, request, jsonify
from flask_jwt_extended import jwt_required, get_jwt_identity
from services.claim_service import ClaimService

claim_bp = Blueprint('claims', __name__)

@claim_bp.route('/', methods=['POST'])
@jwt_required()
def create_claim():
    """Create a new claim request"""
    try:
        user_id = get_jwt_identity()
        data = request.get_json()
        
        lost_item_id = data.get('lost_item_id')
        found_item_id = data.get('found_item_id')
        
        if not lost_item_id or not found_item_id:
            return jsonify({'error': 'Lost item ID and found item ID are required'}), 400
        
        claim = ClaimService.create_claim(lost_item_id, found_item_id, user_id)
        
        return jsonify({
            'message': 'Claim submitted successfully',
            'claim': claim.to_dict()
        }), 201
        
    except ValueError as e:
        return jsonify({'error': str(e)}), 400
    except Exception as e:
        return jsonify({'error': 'Failed to create claim', 'details': str(e)}), 500

@claim_bp.route('/my-claims', methods=['GET'])
@jwt_required()
def get_my_claims():
    """Get current user's claims"""
    try:
        user_id = get_jwt_identity()
        claims = ClaimService.get_user_claims(user_id)
        
        return jsonify({
            'claims': [claim.to_dict() for claim in claims]
        }), 200
        
    except Exception as e:
        return jsonify({'error': 'Failed to get claims', 'details': str(e)}), 500

@claim_bp.route('/<int:claim_id>', methods=['GET'])
@jwt_required()
def get_claim(claim_id):
    """Get claim by ID"""
    try:
        claim = ClaimService.get_claim_by_id(claim_id)
        
        if not claim:
            return jsonify({'error': 'Claim not found'}), 404
        
        return jsonify({'claim': claim.to_dict()}), 200
        
    except Exception as e:
        return jsonify({'error': 'Failed to get claim', 'details': str(e)}), 500
