from flask import Flask, session
import os
from datetime import timedelta
from controller.studentController import student
from controller.adminController import admin
from model.DBUtil import db

app = Flask(__name__)


@app.route('/')
def hello_world():
    return 'Hello World!'


# 配置数据库
app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql://root:eroch123@112.126.102.75:3306/cmajorminiProgram'  # 指定数据库地址、用户名、密码
app.config['SQLALCHEMY_TRACK_MODIFICATION'] = False
app.config['SQLALCHEMY_COMMIT_TEARDOWN'] = True
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = True
db.init_app(app)
app.config['SECRET_KEY'] = 'sessionKEY123'
app.config['PERMANENT_SESSION_LIFETIME'] = timedelta(days=7)  # 设置session的保存时间。

app.register_blueprint(student, url_prefix='/student')
app.register_blueprint(admin, url_prefix='/admin')

if __name__ == '__main__':
    app.run()
