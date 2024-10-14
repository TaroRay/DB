from flask import Blueprint, render_template
import mysql.connector

join_bp = Blueprint('join_bp', __name__)

# Database configuration
db_config = {
    'user': 'root',
    'password': 'Lucas8787',
    'host': 'localhost',
    'database': 'testdb'
}

@join_bp.route('/join', methods=['GET'])
def join_tables():
    try:
        # Connect to the database
        conn = mysql.connector.connect(**db_config)
        cursor = conn.cursor(dictionary=True)

        # SQL JOIN query
        query = """
        SELECT 
            ed.id AS post_id,
            ed.student_id,
            ed.post,
            s.score,
            g.gender
        FROM 
            example_data ed
        INNER JOIN 
            score s ON ed.student_id = s.student_id
        INNER JOIN 
            gender g ON ed.student_id = g.student_id;
        """

        # Execute the query
        cursor.execute(query)

        # Fetch all results
        results = cursor.fetchall()

        # Render results to HTML template
        return render_template('join_result.html', merged_data=results)

    except mysql.connector.Error as err:
        return f"Error: {err}", 500

    finally:
        # Close cursor and connection
        cursor.close()
        conn.close()