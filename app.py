from flask import Flask, request, render_template

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/profile')
def profile():
    username = request.args.get('username', '')
    return render_template('index.html', username=username)

if __name__ == '__main__':
    app.run(debug=True)
