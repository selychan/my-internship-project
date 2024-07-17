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
    
@app.route("/really_unsafe")
def really_unsafe():
    name = request.args.get("name")
    age = request.args.get("age")
    # ruleid: unescaped-template-extension
    return render_template("unsafe.txt", name=name, age=age)


if __name__ == '__main__':
    app.run(debug=True)

app.run(host="0.0.0.0")
