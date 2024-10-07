from flask import Blueprint, request, render_template
import mysql.connector

# 設置 Blueprint
searchID_bp = Blueprint('searchID_bp', __name__)

# 資料庫連接配置
db_config = {
    'user': 'root',
    'password': 'Lucas8787',  # 你的資料庫密碼
    'host': 'localhost',
    'database': 'testdb'  # 你的資料庫名稱
}

# 搜尋文章的路由
@searchID_bp.route('/search', methods=['GET'])
def search_post():
    # 從請求中取得 post_id（搜尋的ID）
    post_id = request.args.get('post_id')
    
    # 如果沒有提供 post_id，返回錯誤
    if not post_id:
        return "Post ID is required", 400
    
    # 連接資料庫
    conn = mysql.connector.connect(**db_config)
    cursor = conn.cursor(dictionary=True)  # 使用字典格式返回資料
    
    try:
        # SQL 查詢語句
        query = "SELECT * FROM example_data WHERE id = %s"
        cursor.execute(query, (post_id,))  # 執行查詢
        
        # 取得查詢結果
        post = cursor.fetchone()
        
        # 檢查是否找到對應的資料
        if post:
            return render_template('search_result.html', post=post)  # 顯示搜尋結果
        else:
            return "Post not found", 404  # 如果沒有找到對應資料，返回 404
    finally:
        # 關閉資料庫連接
        cursor.close()
        conn.close()