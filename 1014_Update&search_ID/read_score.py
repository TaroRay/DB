from flask import Blueprint, render_template
import mysql.connector

read_score_bp = Blueprint('read_score_bp', __name__)

db_config = {
    'user': 'root',
    'password': 'Lucas8787',
    'host': 'localhost',
    'database': 'testdb'
}

@read_score_bp.route('/')
def index_score():
    conn = mysql.connector.connect(**db_config)
    cursor = conn.cursor(dictionary=True)
    
    select_query = "SELECT student_id, score FROM score"
    cursor.execute(select_query)
    posts = cursor.fetchall()
    
    cursor.close()
    conn.close()

    # Render the posts with the add/delete functionality
    return render_template('index_score.html', posts=posts)
