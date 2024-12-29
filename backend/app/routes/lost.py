from flask import Blueprint, request, jsonify
from werkzeug.utils import secure_filename
import os

lost_bp = Blueprint('lost', __name__)
UPLOAD_FOLDER = 'static/uploads'

# Ensure the upload folder exists
os.makedirs(UPLOAD_FOLDER, exist_ok=True)

@lost_bp.route('/upload-lost', methods=['POST'])
def upload_lost_item():
    item_name = request.form.get('itemName')
    description = request.form.get('itemDescription')
    location = request.form.get('locationLost')
    contact = request.form.get('contactInfo')
    item_image = request.files.get('itemImage')

    if item_image:
        # Save the uploaded image
        filename = secure_filename(item_image.filename)
        image_path = os.path.join(UPLOAD_FOLDER, filename)
        item_image.save(image_path)

        # Save item details to the database (mocked here)
        # Example response
        return jsonify({
            'message': 'Lost item successfully uploaded!',
            'data': {
                'item_name': item_name,
                'description': description,
                'location': location,
                'contact': contact,
                'image_path': image_path
            }
        }), 201

    return jsonify({'error': 'Image upload failed.'}), 400
