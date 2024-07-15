from flask import Flask, request, render_template, render_template_string
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

@app.route('/xss')
def xss():
    user_input = request.args.get('input', '')
    return render_template_string(f'<h1>{user_input}</h1>')


if __name__ == '__main__':
    app.run(debug=True)
