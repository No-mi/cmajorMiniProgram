from flask import Flask

from controller.studentController import student
from controller.teacherController import teacher
from model.DBUtil import db

app = Flask(__name__)

@app.route('/')
def hello_world():
    return 'Hello World!'




#配置数据库
app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql://root:eroch123@112.126.102.75:3306/cmajorminiProgram' #指定数据库地址、用户名、密码
app.config['SQLALCHEMY_TRACK_MODIFICATION'] = False
app.config['SQLALCHEMY_COMMIT_TEARDOWN'] = True
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = True
db.init_app(app)



app.register_blueprint(student,url_prefix='/student')
app.register_blueprint(teacher,url_prefix = '/teacher')



if __name__ == '__main__':
    app.run()
