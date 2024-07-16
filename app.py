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
    
@app.route("/route_param_format/<route_param>")
def route_param_format(route_param):
    print("blah")
    # ruleid:raw-html-format
    return "<a href='{}'>Click me!</a>".format(route_param)


if __name__ == '__main__':
    app.run(debug=True)
