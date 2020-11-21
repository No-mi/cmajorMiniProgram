from flask import Blueprint, request
from model.studentDB import getStudentUserByUserName, InsertStudent
from model.modelDB import StudentUser
student = Blueprint("student", __name__)    # 实例化student蓝图

@student.route('/getInfo')
def getStudentInfo():
    user=getStudentUserByUserName("nomi")
    return user.to_json()

@student.route('/insertStudentUser',methods=['GET'])
def insertStudentUser():
    username=request.args['username']
    student_id=request.args['student_id']
    InsertStudent(username,student_id)
    return "OK"