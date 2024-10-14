from flask import Blueprint, request, redirect, url_for
import mysql.connector

update_gender_bp = Blueprint('update_gender_bp', __name__)

db_config = {
    'user': 'root',
    'password': 'Lucas8787',
    'host': 'localhost',
    'database': 'testdb'
}

@update_gender_bp.route('/update_gender/<int:student_id>', methods=['POST'])
def update_gender_post(student_id):
    new_content = request.form.get(f'gender_{student_id}')  # 更新這一行
    
    if not new_content:
        return "No content to update", 400
    
    conn = mysql.connector.connect(**db_config)
    cursor = conn.cursor()

    update_query = "UPDATE gender SET gender = %s WHERE student_id = %s"  # 更新這一行
    
    cursor.execute(update_query, (new_content, student_id))
    conn.commit()
    
    cursor.close()
    conn.close()
    
    return redirect(url_for('read_gender_bp.index_gender'))  # 更新這一行