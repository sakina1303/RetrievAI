from flask import Blueprint, jsonify
from flask_jwt_extended import jwt_required
from utils.decorators import admin_required
from services.claim_service import ClaimService
from services.item_service import ItemService
from repositories.user_repository import UserRepository

admin_bp = Blueprint('admin', __name__)
item_service = ItemService()

@admin_bp.route('/users', methods=['GET'])
@jwt_required()
@admin_required()
def get_all_users():
    """Get all users (admin only)"""
    try:
        users = UserRepository.get_all()
        return jsonify({
            'users': [user.to_dict() for user in users]
        }), 200
    except Exception as e:
        return jsonify({'error': 'Failed to get users', 'details': str(e)}), 500

@admin_bp.route('/claims', methods=['GET'])
@jwt_required()
@admin_required()
def get_all_claims():
    """Get all claims (admin only)"""
    try:
        claims = ClaimService.get_all_claims()
        return jsonify({
            'claims': [claim.to_dict() for claim in claims]
        }), 200
    except Exception as e:
        return jsonify({'error': 'Failed to get claims', 'details': str(e)}), 500

@admin_bp.route('/claims/pending', methods=['GET'])
@jwt_required()
@admin_required()
def get_pending_claims():
    """Get pending claims (admin only)"""
    try:
        claims = ClaimService.get_pending_claims()
        return jsonify({
            'claims': [claim.to_dict() for claim in claims]
        }), 200
    except Exception as e:
        return jsonify({'error': 'Failed to get pending claims', 'details': str(e)}), 500

@admin_bp.route('/claims/<int:claim_id>/approve', methods=['POST'])
@jwt_required()
@admin_required()
def approve_claim(claim_id):
    """Approve a claim (admin only)"""
    try:
        claim = ClaimService.approve_claim(claim_id)
        return jsonify({
            'message': 'Claim approved successfully',
            'claim': claim.to_dict()
        }), 200
    except ValueError as e:
        return jsonify({'error': str(e)}), 400
    except Exception as e:
        return jsonify({'error': 'Failed to approve claim', 'details': str(e)}), 500

@admin_bp.route('/claims/<int:claim_id>/reject', methods=['POST'])
@jwt_required()
@admin_required()
def reject_claim(claim_id):
    """Reject a claim (admin only)"""
    try:
        claim = ClaimService.reject_claim(claim_id)
        return jsonify({
            'message': 'Claim rejected successfully',
            'claim': claim.to_dict()
        }), 200
    except ValueError as e:
        return jsonify({'error': str(e)}), 400
    except Exception as e:
        return jsonify({'error': 'Failed to reject claim', 'details': str(e)}), 500

@admin_bp.route('/items/lost', methods=['GET'])
@jwt_required()
@admin_required()
def admin_get_all_lost_items():
    """Get all lost items (admin only)"""
    try:
        items = item_service.get_all_lost_items()
        return jsonify({
            'items': [item.to_dict() for item in items]
        }), 200
    except Exception as e:
        return jsonify({'error': 'Failed to get lost items', 'details': str(e)}), 500

@admin_bp.route('/items/found', methods=['GET'])
@jwt_required()
@admin_required()
def admin_get_all_found_items():
    """Get all found items (admin only)"""
    try:
        items = item_service.get_all_found_items()
        return jsonify({
            'items': [item.to_dict() for item in items]
        }), 200
    except Exception as e:
        return jsonify({'error': 'Failed to get found items', 'details': str(e)}), 500
