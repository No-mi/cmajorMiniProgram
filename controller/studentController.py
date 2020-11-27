from flask import Blueprint, request

from model.couresDB import getCoursesByStudentId
from model.studentDB import getStudentUserByUserName, insertStudent, deleteStudent,updateStudentInfo
from model.modelDB import StudentUser
student = Blueprint("student", __name__)    # 实例化student蓝图

@student.route('/getInfo',methods=["GET"])
def getStudentInfo():
    user=getStudentUserByUserName(request.args['username'])
    return user.to_json()

@student.route('/insertStudentUser',methods=['GET'])
def insertStudentUser():
    username=request.args['username']
    student_id=request.args['student_id']
    insertStudent(username,student_id)
    return "OK"

@student.route('/deleteStudentUser',methods=['GET'])
def deleteStudentUser():
    student_id=request.args['student_id']
    deleteStudent(student_id)
    return "OK"

@student.route('/updateStudentInfo',methods=['GET'])
def updateStudentUserInfo():
    username=request.args['username']
    student_id=request.args['student_id']
    updateStudentInfo(student_id,username)
    return "OK"
@student.route('/getCourse',methods=['GET'])
def getCourse():
    student_id=request.args['student_id']
    courses=getCoursesByStudentId(student_id)
    for i in courses:
        print(i.to_json())
    return "OK"