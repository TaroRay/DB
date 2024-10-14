from flask import Flask
from create_score import create_score_bp
from read_score import read_score_bp
from update_score import update_score_bp  # Import the update blueprint
from delete_score import delete_score_bp


app = Flask(__name__)

# Register the blueprints
app.register_blueprint(create_score_bp)
app.register_blueprint(read_score_bp)
app.register_blueprint(update_score_bp)  # Register the update blueprint
app.register_blueprint(delete_score_bp)

if __name__ == '__main__':
    app.run(debug=True)
