from flask import Blueprint, request, redirect, url_for
import mysql.connector

delete_gender_bp = Blueprint('delete_gender_bp', __name__)

db_config = {
    'user': 'root',
    'password': 'Lucas8787',
    'host': 'localhost',
    'database': 'testdb'
}

@delete_gender_bp.route('/delete_gender', methods=['POST'])
def delete_gender_posts():
    selected_gender_ids = request.form.getlist('student_id')  # 確保這裡的名稱與 HTML 中的 input 相符
    
    if selected_gender_ids:
        conn = mysql.connector.connect(**db_config)
        cursor = conn.cursor()
        
        delete_query = "DELETE FROM gender WHERE student_id IN (%s)" % ','.join(['%s'] * len(selected_gender_ids))
        cursor.execute(delete_query, tuple(selected_gender_ids))
        
        conn.commit()  # 提交更改
        cursor.close()  # 關閉游標
        conn.close()  # 關閉資料庫連接
    
    return redirect(url_for('read_gender_bp.index_gender'))  # 返回主頁面
       