from flask import Blueprint, request, redirect, url_for
import mysql.connector

update_score_bp = Blueprint('update_score_bp', __name__)

db_config = {
    'user': 'root',
    'password': 'Lucas8787',
    'host': 'localhost',
    'database': 'testdb'
}

@update_score_bp.route('/update_score/<int:student_id>', methods=['POST'])
def update_score_post(student_id):
    # 確保從表單中取得正確的值
    new_score = request.form.get(f'post_{student_id}')  # 使用 f-string 來根據 student_id 動態取得表單資料
    
    # 檢查是否有輸入資料，沒有的話返回錯誤
    if not new_score:
        return "No content to update", 400  # 返回 400 錯誤，告知無內容
    
    # 連接到資料庫並更新內容
    conn = mysql.connector.connect(**db_config)
    cursor = conn.cursor()

    update_query = "UPDATE score SET score = %s WHERE student_id = %s"  # 更新條件是 student_id
    
    # 執行更新語句
    cursor.execute(update_query, (new_score, student_id))
    conn.commit()  # 提交更改
    
    cursor.close()
    conn.close()
    
    # 更新完成後，重定向到主頁面
    return redirect(url_for('read_score_bp.index_score'))  # 確保這裡的 endpoint 正確