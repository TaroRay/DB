from flask import Blueprint, request, redirect, url_for
import mysql.connector

# 設置 Blueprint
create_gender_bp = Blueprint('create_gender_bp', __name__)

# 資料庫連接配置
db_config = {
    'user': 'root',
    'password': 'Lucas8787',  # 你的資料庫密碼
    'host': 'localhost',
    'database': 'testdb'  # 你的資料庫名稱
}

# 添加性別的路由
@create_gender_bp.route('/add_gender', methods=['POST'])
def add_gender_post():
    # 獲取性別
    gender = request.form['gender']  # 使用表單的名稱 'gender'

    # 連接到資料庫
    conn = mysql.connector.connect(**db_config)
    cursor = conn.cursor()

    try:
        # 插入數據，假設學生 ID 是自動生成的，因此只插入 gender
        insert_query = "INSERT INTO gender (gender) VALUES (%s)"
        cursor.execute(insert_query, (gender,))
        conn.commit()
    except Exception as e:
        print(f"Error: {e}")
        conn.rollback()
    finally:
        cursor.close()
        conn.close()

    return redirect(url_for('read_gender_bp.index_gender'))  # 使用正確的端點名稱