
from watchlist import db,app
from watchlist.models import *
import click



# 自定义命令
# 建立空数据库
@app.cli.command() # 注册为命令
@click.option('--drop',is_flag=True,help="先删除在创建")
def initdb(drop):
    if drop:
        db.drop_all()
    db.create_all()
    click.echo("初始化数据库完成！")

# 向数据库插入数据
@app.cli.command()
def forge():
    movie = [
        {'title':"大赢家",'year':"2020"},
        {'title':"囧妈",'year':"2020"},
        {'title':"疯狂外星人",'year':"2019"},
        {'title':"战狼",'year':"2017"}
    ]
    for m in movie:
        mov = Movie(title=m['title'],year=m['year'])
        db.session.add(mov)
    db.session.commit()
    click.echo("导入数据完成！")

# 创建账号
@app.cli.command()
@click.option('--username',prompt=True,help='登录的用户名')
@click.option('--password',prompt=True,help='登录的密码',confirmation_prompt=True,hide_input=True)
def admin(username,password):
    user = User.query.first()
    if user is not None:
        click.echo('更新管理员用户')
        user.username = username
        user.set_password(password)
    else:
        click.echo('创建管理员账户')
        user = User(username=username,name='Admin')
        user.set_password(password)
        db.session.add(user)
    db.session.commit()
    click.echo('管理员账号更新完成！')