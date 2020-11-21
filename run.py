from flask import Flask, Blueprint
from flask_sqlalchemy import SQLAlchemy

from controller.studentController import student
from controller.teacherController import teacher

app = Flask(__name__)

@app.route('/')
def hello_world():
    return 'Hello World!'


app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql+pymysql://root:@127.0.0.1/monitor_system'



app.register_blueprint(student,url_prefix='/student')
app.register_blueprint(teacher,url_prefix = '/teacher')



if __name__ == '__main__':
    app.run()
