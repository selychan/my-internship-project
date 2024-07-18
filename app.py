from flask import Flask, request, render_template
import sqlite3

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/profile')
def profile():
    username = request.args.get('username', '')
    return render_template('index.html', username=username)

@app.route('/search')
def search():
    query = request.args.get('query', '')
    conn = sqlite3.connect('database.db')
    cursor = conn.cursor()
    cursor.execute(f"SELECT * FROM users WHERE name = '{query}'")
    results = cursor.fetchall()
    conn.close()
    return str(results)
    
@app.route('/vulnerable')
def vulnerable_view():
    user_input = request.args.get('user_input', '')
    response_html = f"<html><body>User input: {user_input}</body></html>"
    return response_html
    

@app.route('/greet', methods=['GET'])
def greet():
    name = request.args.get('name')
    greeting = f"<h1>Hello, {name}!</h1>"  # User input is directly included in HTML
    return greeting

if __name__ == '__main__':
    app.run(debug=True)

app.run(host="0.0.0.0")
