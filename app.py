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
    
@app.route("/loginpage")
def render_login_page(thing):
    # ruleid:directly-returned-format-string
    return '''
<p>{}</p>
<form method="POST" style="margin: 60px auto; width: 140px;">
    <p><input name="username" type="text" /></p>
    <p><input name="password" type="password" /></p>
    <p><input value="Login" type="submit" /></p>
</form>
    '''.format(thing)


if __name__ == '__main__':
    app.run(debug=True)

app.run(host="0.0.0.0")
