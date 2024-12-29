from flask import Flask
from app.routes.found import found_bp  # Adjusted to a relative import
from app.routes.lost import lost_bp    # Adjusted to a relative import
from app import db

# Initialize the Flask application
app = Flask(__name__)

# Configure the database (adjust the URI as per your actual database config)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///site.db'  # Example using SQLite
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db.init_app(app)

# Register Blueprints
app.register_blueprint(found_bp, url_prefix='/found')
app.register_blueprint(lost_bp, url_prefix='/lost')

# Run the app
if __name__ == "__main__":
    app.run(debug=True)
