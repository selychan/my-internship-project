import json
import flask
from flask import Flask, request, make_response
from somewhere import fxn
app = Flask(__name__)

@app.route('/XSS_param', methods =['GET'])
def XSS1():
    param = request.args.get('param', 'not set')

    other_var = param

    html = open('templates/XSS_param.html').read()
    # ruleid: make-response-with-unknown-content
    resp = make_response(html.replace('{{ param }}', other_var))
    return resp
