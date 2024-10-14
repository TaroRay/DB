from flask import Flask
from create_gender import create_gender_bp
from read_gender import read_gender_bp
from update_gender import update_gender_bp  # Import the update blueprint
from delete_gender import delete_gender_bp


app = Flask(__name__)

# Register the blueprints
app.register_blueprint(create_gender_bp)
app.register_blueprint(read_gender_bp)
app.register_blueprint(update_gender_bp)  # Register the update blueprint
app.register_blueprint(delete_gender_bp)

if __name__ == '__main__':
    app.run(debug=True)