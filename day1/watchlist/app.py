from flask import Flask,url_for

app = Flask(__name__)

# @app.route('/')
# @app.route('/index')
# def index():
#     return "hello Flask"

@app.route('/index/<name>')
def index(name):
    print(url_for('index',name='hahaha'))
    return "hello Flask,%s"%name    