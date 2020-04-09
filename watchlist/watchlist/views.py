
from flask import Flask,url_for,render_template,request,flash,redirect,url_for
from flask_login import login_user,logout_user,login_required,current_user
from watchlist.models import *
from watchlist import db,app

# views 视图函数
@app.route('/', methods=['GET','POST'])
def index():
    movie = Movie.query.all()
    if request.method == 'POST':
        if not current_user.is_authenticated:
            return redirect(url_for('index'))
        g_title = request.form.get('title')
        g_year = request.form.get('year')
        # 验证数据
        if not g_title or not g_year or len(g_year)>4 or len(g_title)>20:
            flash('输入错误！')
            return redirect(url_for('index'))
        # 将数据保存到数据库    
        mov = Movie(title=g_title,year=g_year)
        db.session.add(mov)
        db.session.commit()
        flash('提交成功！')
        return redirect(url_for('index'))

    return render_template('index.html',movie=movie)

# 更新
@app.route('/movie/edit/<int:movie_id>',methods=['GET','POST'])
@login_required
def edit(movie_id):
    movie = Movie.query.get_or_404(movie_id)
    if request.method == 'POST':
        title = request.form.get('title')
        year = request.form.get('year')
        if not title or not year or len(year)>4 or len(title)>60:
            flash('输入有误！')
            return redirect(url_for('edit',movie_id=movie_id))
        movie.title = title
        movie.year = year
        db.session.commit()
        flash('电影更新完成！')
        return redirect(url_for('index'))
    return render_template('edit.html',movie=movie)


# 删除
@app.route('/delete/<int:movie_id>',methods=['GET','POST'])
@login_required
def delete(movie_id):
    movie = Movie.query.get_or_404(movie_id)
    db.session.delete(movie)
    db.session.commit()
    flash('删除成功！')
    return redirect(url_for('index'))

# 登录
@app.route('/login/',methods=['POST','GET'])
def login():
    if request.method == 'POST':
        username = request.form['username']
        password = request.form['password']
        if not username or not password:
            flash('输入有误！')
            return redirect(url_for('login'))
        user = User.query.first()
        if username == user.username and user.validate_password(password):
            login_user(user)
            flash('登录成功！')
            return redirect(url_for('index'))
        flash('验证失败！')
        return redirect(url_for('login.html'))
    return render_template('login.html')


# 退出
@app.route('/login')
def logout():
    logout_user
    flash('退出成功！')
    return redirect(url_for('index'))

# 设置
@app.route('/setting',methods=['POST','GET'])
def setting():
    if request.method == 'POST':
        name = request.form['name']
        current_user.name = name
        db.session.commit()
        flash('设置完成！')
        return redirect(url_for('index'))

    return render_template('setting.html')


