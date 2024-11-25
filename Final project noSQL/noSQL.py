from flask import Flask, render_template, request, redirect, url_for, session
from bson.objectid import ObjectId
from config import collection  # Import collection from config.py
from update import update_bp  # Import the update blueprint
from delete import delete_bp  # Import the delete blueprint

app = Flask(__name__)
app.secret_key = 'your_secret_key'
app.register_blueprint(update_bp)
app.register_blueprint(delete_bp)

# Display documents (Read)
@app.route('/')
def index():
    show_all = session.get('show_all', False)
    data = list(collection.find({})) if show_all else []
    for doc in data:
        doc['_id'] = str(doc['_id'])
    return render_template('index.html', data=data, results=None, show_all=show_all)

# Create a new document (Create)
@app.route('/create', methods=['GET', 'POST'])
def create():
    if request.method == 'POST':
        name = request.form.get('name')
        number = request.form.get('number')
        first = request.form.get('first')
        second = request.form.get('second')
        third = request.form.get('third')
        new_doc = {'name': name, 'number':number, 'first': first, 'second':second, 'third':third}
        collection.insert_one(new_doc)
        return redirect(url_for('index'))
    return render_template('create.html')

# Search documents (Read with keyword)
@app.route('/search', methods=['POST'])
def search():
    query_text = str(request.form.get("query", ""))
    regex_query = {"$regex": query_text, "$options": "i"}
    query = {"$or": [{field: regex_query} for field in ["name", "description", "hostname", "startTime", "startTimeLocal", "pid"]]}

    results = list(collection.find(query))
    for result in results:
        result['_id'] = str(result['_id'])

    # 搜尋結果，不顯示全部資料
    return render_template('index.html', data=[], results=results, show_all=session.get('show_all', False))

# Toggle show_all feature
@app.route('/show_all', methods=['GET'])
def show_all():
    session['show_all'] = not session.get('show_all', False)
    return redirect(url_for('index'))

# Delete a document (Delete)
@app.route('/delete/<id>', methods=['POST'])
def delete(id):
    try:
        collection.delete_one({"_id": ObjectId(id)})
        return redirect(url_for('index'))
    except Exception as e:
        return str(e), 400

# Calculate average scores
@app.route('/average')
def calculate_average():
    records = collection.find()
    averages = []

    for record in records:
        try:
            # 確保所有成績為數字型別
            first = float(record.get('first', 0))
            second = float(record.get('second', 0))
            third = float(record.get('third', 0))
            # 計算平均值
            average = (first + second + third) / 3
            averages.append({
                'name': record.get('name', '未知'),
                'average': round(average, 2)
            })
        except ValueError:
            # 如果成績不是數字，跳過
            continue

    return render_template('average.html', averages=averages)
@app.route('/class_averages')
def calculate_class_averages():
    records = collection.find()
    total_first, total_second, total_third = 0, 0, 0
    count = 0

    for record in records:
        try:
            first = float(record.get('first', 0))
            second = float(record.get('second', 0))
            third = float(record.get('third', 0))
            total_first += first
            total_second += second
            total_third += third
            count += 1
        except ValueError:
            continue  # Skip records with invalid data

    class_averages = {
        'first_avg': round(total_first / count, 2) if count > 0 else 0,
        'second_avg': round(total_second / count, 2) if count > 0 else 0,
        'third_avg': round(total_third / count, 2) if count > 0 else 0
    }

    return render_template('class_averages.html', class_averages=class_averages)

if __name__ == '__main__':
    app.run(debug=True)
