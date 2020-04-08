import os,sys
from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_login import LoginManager

WIN = sys.platform.startswith('win') # 判断是不是windows系统
if WIN:
    prefix = "sqlite:///" # window系统
else:
    prefix = "sqlite:////" # Mac linux系统



app = Flask(__name__)

app.config['SQLALCHEMY_DATABASE_URI'] =  prefix + os.path.join(os.path.dirname(app.root_path),'data.db')
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False  # 对内存做优化
app.config['SECRET_KEY'] = os.getenv('SECRET_KEY','dev') 


db = SQLAlchemy(app) # 初始化app
login_manager = LoginManager(app) # 实例化扩展类
@login_manager.user_loader
def load_user(user_id): # 创建用户加载回调函数，接收用户id作为参数
    from watchlist.models import User
    user = User.query.get(user_id)
    return user
# 如果操作了只有登录才有的操作，系统会跳转到login页
login_manager.login_view = 'login'



# 模板上下文出力函数
@app.context_processor
def common_user():
    from watchlist.models import User
    user = User.query.first()
    return dict(user=user)

from watchlist import views, errors,commands