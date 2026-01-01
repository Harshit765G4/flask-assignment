from flask import Flask, jsonify, render_template, request, redirect
from pymongo import MongoClient
import json

app = Flask(__name__)

@app.route('/api')
def api_data():
    with open('data.json', 'r') as file:
        data = json.load(file)
    return jsonify(data)

client = MongoClient("mongodbKey")
db = client["studentDB"]
collection = db["students"]

@app.route('/', methods=['GET', 'POST'])
def form():
    error = None
    if request.method == 'POST':
        try:
            name = request.form['name']
            email = request.form['email']
            collection.insert_one({
                "name": name,
                "email": email
            })
            return redirect('/success')
        except Exception as e:
            error = str(e)

    return render_template('form.html', error=error)

@app.route('/success')
def success():
    return "Data submitted successfully"

if __name__ == '__main__':
    app.run(debug=True)
