from flask import Blueprint, render_template
import mysql.connector

read_gender_bp = Blueprint('read_gender_bp', __name__)

db_config = {
    'user': 'root',
    'password': 'Lucas8787',
    'host': 'localhost',
    'database': 'testdb'
}

@read_gender_bp.route('/')
def index_gender():
    conn = mysql.connector.connect(**db_config)
    cursor = conn.cursor(dictionary=True)
    
    select_query = "SELECT student_id, gender FROM gender"
    cursor.execute(select_query)
    posts = cursor.fetchall()
    
    cursor.close()
    conn.close()

    # Render the posts with the add/delete functionality
    return render_template('index_gender.html', posts=posts)