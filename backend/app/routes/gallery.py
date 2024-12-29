from flask import Blueprint, jsonify

gallery_bp = Blueprint('gallery', __name__)

@gallery_bp.route('/get-gallery-items', methods=['GET'])
def get_gallery_items():
    # Fetch items from the database (mocked for now)
    items = [
        {
            'item_name': 'Black Wallet',
            'description': 'Black wallet with silver logo',
            'location': 'Classroom 101',
            'image_path': '/static/uploads/sample-item.jpg'
        },
        # Add more sample items here
    ]
    return jsonify({'items': items})
