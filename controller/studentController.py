import json

from flask import Blueprint, request, session

from model.applicationDB import insertApplicqtion, updateApplicationByOpenID, getApplicationByOpenID
from model.couresDB import getCoursesByStudentId
from model.studentDB import getStudentUserByUserName, insertStudent, deleteStudent, updateStudentInfo
from model.modelDB import StudentUser
from server.studentServer import checkUser

student = Blueprint("student", __name__)  # 实例化student蓝图


@student.route('/getInfo', methods=["GET"])
def getStudentInfo():
    user = getStudentUserByUserName(request.args['username'])
    return user.to_json()


@student.route('/insertStudentUser', methods=['GET'])
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

@student.route('/updateStudentInfo', methods=['GET'])
def updateStudentUserInfo():
    username = request.args['username']
    student_id = request.args['student_id']
    updateStudentInfo(student_id, username)
    return "OK"


@student.route('/getCourse', methods=['GET'])
def getCourse():
    student_id = request.args['student_id']
    courses = getCoursesByStudentId(student_id)
    return json.dumps(list(map(lambda x: x.cId, courses)))


@student.route('/setSession', methods=['GET'])
def setSession():
    session.permanent = True
    session['username'] = 'sess'
    return 'sessionTest'


@student.route('/checkSession', methods=['GET'])
def checkSession():
    return session.get('username')


@student.route('/setApplication', methods=['POST'])
def setCourse():
    if checkUser("111") is False:
        return 0
    studentName = request.form.get("studentName")
    # print("student", studentName)
    openID = request.form.get("openID")
    studentID = request.form.get("studentID")
    institute = request.form.get("institute")
    major = request.form.get("major")
    grade = request.form.get("grade")
    downGrade = int(request.form.get("downGrade"))
    # print("dwonGrade", downGrade)
    choiceAfterGraduating = int(request.form.get("choiceAfterGraduating"))
    doctor = int(request.form.get("doctor"))
    ID = int(request.form.get("ID"))
    courses = getCoursesByStudentId(studentID)
    insertApplicqtion(openID, studentName, studentID, institute, major, grade, downGrade, choiceAfterGraduating, doctor,
                      ID,
                      courses)
    return "OK"


@student.route('/updateApplication', methods=['POST'])
def updateApplication():
    studentName = request.form.get("studentName")
    print("student", studentName)
    openID = request.form.get("openID")
    studentID = request.form.get("studentID")
    institute = request.form.get("institute")
    major = request.form.get("major")
    downGrade = int(request.form.get("downGrade"))
    grade = request.form.get("grade")
    print("dwonGrade", downGrade)
    choiceAfterGraduating = int(request.form.get("choiceAfterGraduating"))
    doctor = int(request.form.get("doctor"))
    ID = int(request.form.get("ID"))
    courses = getCoursesByStudentId(studentID)
    updateApplicationByOpenID(openID, studentName, studentID, institute, major, grade, downGrade,
                              choiceAfterGraduating, doctor, ID, courses)
    return "OK"


@student.route('/login', methods=['GET'])
def login():
    code = request.args['code']


@student.route('/getApplication', methods=['GET'])
def getApplication():
    openID = request.args.get("openID")
    appli = getApplicationByOpenID(openID)
    return appli.to_json()
