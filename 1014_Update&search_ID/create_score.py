from flask import Blueprint, request, redirect, url_for
import mysql.connector

# 設置 Blueprint
create_score_bp = Blueprint('create_score_bp', __name__)

# 資料庫連接配置
db_config = {
    'user': 'root',
    'password': 'Lucas8787',  # 你的資料庫密碼
    'host': 'localhost',
    'database': 'testdb'  # 你的資料庫名稱
}

# 添加分數的路由
@create_score_bp.route('/add_score', methods=['POST'])
def add_score_post():
    # 獲取分數
    score = request.form['post']  # 使用表單的名稱 'post'

    # 連接到資料庫
    conn = mysql.connector.connect(**db_config)
    cursor = conn.cursor()

    try:
        # 插入數據
        insert_query = "INSERT INTO score (score) VALUES (%s)"
        cursor.execute(insert_query, (score,))
        conn.commit()
    except Exception as e:
        print(f"Error: {e}")
        conn.rollback()
    finally:
        cursor.close()
        conn.close()

    return redirect(url_for('read_score_bp.index_score'))  # 使用正確的端點名稱
