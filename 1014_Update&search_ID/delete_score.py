from flask import Blueprint, request, redirect, url_for
import mysql.connector

delete_score_bp = Blueprint('delete_score_bp', __name__)

db_config = {
    'user': 'root',
    'password': 'Lucas8787',
    'host': 'localhost',
    'database': 'testdb'
}

@delete_score_bp.route('/delete_score', methods=['POST'])
def delete_score_posts():
    selected_score_ids = request.form.getlist('student_id')
    
    if selected_score_ids:
        conn = mysql.connector.connect(**db_config)
        cursor = conn.cursor()
        
        delete_query = "DELETE FROM score WHERE student_id IN (%s)" % ','.join(['%s'] * len(selected_score_ids))
        cursor.execute(delete_query, tuple(selected_score_ids))
        
        conn.commit()
        cursor.close()
        conn.close()
    
    return redirect(url_for('read_score_bp.index_score'))  # Redirect to the main view
