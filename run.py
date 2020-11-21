from flask import Flask

from controller.studentController import student
from controller.teacherController import teacher
from model.DBUtil import db

app = Flask(__name__)

@app.route('/')
def hello_world():
    return 'Hello World!'


app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql://root:123456@127.0.0.1:3306/demo'
app.config['SQLALCHEMY_TRACK_MODIFICATION'] = False
app.config['SQLALCHEMY_COMMIT_TEARDOWN'] = True
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = True




app.register_blueprint(student,url_prefix='/student')
app.register_blueprint(teacher,url_prefix = '/teacher')
db.init_app(app)


if __name__ == '__main__':
    app.run()
