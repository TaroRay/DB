from flask import Flask, request, redirect, url_for
from pymongo import MongoClient

app = Flask(__name__)

# MongoDB connection (adjust as per your local MongoDB setup)
client = MongoClient('mongodb://localhost:27017/')
db = client['local']  # The database name
collection = db['startup_log']  # The collection name

@app.route('/create', methods=['GET', 'POST'])
def create():
    if request.method == 'POST':
        # Get form data from request
        name = request.form.get('name')
        number = request.form.get('number')
        first = request.form.get('first')
        second = request.form.get('second')
        third = request.form.get('third')
        # Insert the new document into the MongoDB collection
        new_doc = {'name': name, 'number':number, 'first': first, 'second':second, 'third':third}
        collection.insert_one(new_doc)

        


        # Redirect to the index page after successful insertion
        return redirect(url_for('index'))

    # If GET request, show the create form
    return '''
        <form method="POST">
            Name: <input type="text" name="name"><br>
            Description: <input type="text" name="description"><br>
            <input type="submit" value="Create">
        </form>
    '''