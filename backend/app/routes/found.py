from flask import Blueprint, request, redirect, url_for
from flask import render_template

from werkzeug.utils import secure_filename
from backend.app import db, FoundItem
import os

# Blueprint for Found Items
found_bp = Blueprint('found', __name__)

# Function to check allowed file extensions
def allowed_file(filename):
    return '.' in filename and filename.rsplit('.', 1)[1].lower() in {'png', 'jpg', 'jpeg', 'gif'}

# Route to handle submitting a found item
@found_bp.route('/upload', methods=['POST'])
def upload_found_item():
    if request.method == 'POST':
        name = request.form['name']
        description = request.form['description']
        file = request.files['foundImage']
        
        # Check if file is uploaded and has allowed extension
        if file and allowed_file(file.filename):
            filename = secure_filename(file.filename)
            file.save(os.path.join('./backend/static/uploads', filename))  # Save file to uploads folder
            
            # Create a new found item entry
            new_found_item = FoundItem(name=name, description=description, image=filename)
            db.session.add(new_found_item)
            db.session.commit()

            return redirect(url_for('gallery.view_gallery'))
        else:
            return "File type not allowed or no file uploaded!", 400

# Route to get all found items (used in the gallery)
@found_bp.route('/all', methods=['GET'])
def get_all_found_items():
    items = FoundItem.query.all()  # Get all found items from the database
    return render_template('gallery.html', items=items)  # Render the gallery page with items
