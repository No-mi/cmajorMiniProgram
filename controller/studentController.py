from flask import Blueprint
from model.studentDB import getStudentUserByUserName
from model.modelDB import StudentUser
student = Blueprint("student", __name__)    # 实例化student蓝图

@student.route('/')
def getstu():
    return 'stu'

@student.route('/gatInfo')
def getStudentInfo():
    user=getStudentUserByUserName("nomi")
    return user.to_json()