
from watchlist import app
from flask import render_template
from watchlist.models import User

# 错误信息页面
@app.errorhandler(404)
def page_not_found(e):
    user = User.query.first()
    return render_template('404.html')