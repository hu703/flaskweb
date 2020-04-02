from flask import Flask,url_for,render_template

app = Flask(__name__)

# @app.route('/')
# @app.route('/index')
# def index():
#     return "hello Flask"

@app.route('/')
def index():
    name = 'ahu'
    movie = [
        {'title':"大赢家",'year':"2020"},
        {'title':"囧妈",'year':"2020"},
        {'title':"疯狂外星人",'year':"2019"},
        {'title':"战狼",'year':"2017"}
    ]
    return render_template('index.html',name=name,movie=movie)