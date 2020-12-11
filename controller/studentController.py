# -*- coding: UTF-8 -*-
import json
from flask import Blueprint, request, session, send_from_directory
from model.applicationDB import insertApplicqtion, updateApplicationByOpenID, getApplicationByOpenID, deleteOtherFile, \
    deleteSpecialities, setOtherFiles, setSpecialities, ApplicationTransfor, getAllInstitutionInfo
from model.couresDB import getAllCourses
from model.studentCourseDB import setCourseByStudentID, delCourseByStudentID
from model.studentDB import getStudentUserByUserName, insertStudent, deleteStudent, updateStudentInfo
from server.studentServer import checkUser, onLogin, decrypt, getExcel, outputdir

student = Blueprint("student", __name__)  # 实例化student蓝图

@student.route('/getInfo', methods=["GET"])
def getStudentInfo():
    user = getStudentUserByUserName(request.args['username'])
    return user.to_json()

@student.route('/insertStudentUser', methods=['GET'])
def insertStudentUser():
    username = request.args['username']
    student_id = request.args['student_id']
    insertStudent(username, student_id)
    return "OK"

@student.route('/deleteStudentUser', methods=['GET'])
def deleteStudentUser():
    student_id = request.args['student_id']
    deleteStudent(student_id)
    return "OK"

@student.route('/getAllCourses')
def getCourses():
    return json.dumps(getAllCourses())

@student.route('/updateStudentInfo', methods=['GET'])
def updateStudentUserInfo():
    username = request.args['username']
    student_id = request.args['student_id']
    updateStudentInfo(student_id, username)
    return "OK"

@student.route('/checkSession', methods=['GET'])
def checkSession():
    return session.get('username')

@student.route('/setApplication', methods=['POST'])
def setApplication():
    if checkUser("111") is False:
        return 0
    req = json.loads(request.get_data(as_text=True))
    print('req', req)
    studentName = req.get("name")
    openID = decrypt(req.get("openID"))
    studentID = req.get("studentID")
    institute = req.get("institute")
    major = req.get("major")
    grade = req.get("grade")
    downGrade = req.get("downGrade")
    choiceAfterGraduating = req.get("choiceAfterGraduating")
    doctor = req.get("doctor")
    ID = req.get("ID")
    courses = req.get("courses")
    CET = req.get("CET")
    CETScore = req.get("CETScore")
    GPA = req.get("GPA")

    speciality = req.get('specialities')
    CETRecord = req.get('CETRecord')
    otherFile = req.get('otherFiles')
    academicRecord = req.get('academicRecord')
    phoneNumber = req.get('phoneNumber')
    setCourseByStudentID(courses, studentID)
    setOtherFiles(otherFile, studentID)
    setSpecialities(speciality, studentID)
    insertApplicqtion(openID, studentName, studentID, institute, major, grade, downGrade, choiceAfterGraduating, doctor,
                      ID,
                      CET, CETScore, GPA, phoneNumber, academicRecord, CETRecord)
    return "OK"

@student.route('/updateApplication', methods=['POST'])
def updateApplication():
    print("test")
    req = json.loads(request.get_data(as_text=True))
    print('req', req)
    studentName = req.get("name")
    # print("student", studentName)
    openID = decrypt(req.get("openID"))
    studentID = req.get("studentID")
    institute = req.get("institute")
    major = req.get("major")
    grade = req.get("grade")
    downGrade = req.get("downGrade")
    # print("dwonGrade", downGrade)
    choiceAfterGraduating = int(req.get("choiceAfterGraduating"))
    doctor = int(req.get("doctor"))
    ID = int(req.get("ID"))
    courses = req.get("courses")
    CET = req.get("CET")
    CETScore = req.get("CETScore")
    GPA = req.get("GPA")
    phoneNumber = req.get("phoneNumber")
    speciality = req.get('specialities')
    CETRecord = req.get('CETRecord')
    otherFile = req.get('otherFiles')
    print(otherFile)
    academicRecord = req.get('academicRecord')
    updateApplicationByOpenID(openID, studentName, studentID, institute, major, grade, downGrade, choiceAfterGraduating,
                              doctor, ID,
                              CET, CETScore, GPA, phoneNumber, academicRecord, CETRecord)
    delCourseByStudentID(studentID)
    setCourseByStudentID(courses, studentID)
    deleteOtherFile(studentID)
    deleteSpecialities(studentID)
    setOtherFiles(otherFile, studentID)
    setSpecialities(speciality, studentID)

    return getApplicationByOpenID(openID).to_json()


@student.route('/getMajorInfo')
def getMajorInfo():
    return json.dumps(getAllInstitutionInfo())


@student.route('/getApplicationByOpenID', methods=['GET'])
def getAppli():
    openID = decrypt(request.args.get("openID"))
    application = getApplicationByOpenID(openID)
    return ApplicationTransfor(application)


@student.route('/login', methods=['GET'])
def login():
    code = request.args.get("code")
    encryptedData = request.args.get("encryptedData")
    iv = request.args.get("iv")
    return onLogin(code, encryptedData, iv)


@student.route('/check', methods=['GET'])
def c():
    openIDen = request.args.get("openIDEN")
    return decrypt(openIDen)

@student.route('/getZip')
def excel():
    outputdir()
    return send_from_directory("", "out.zip", as_attachment=True)
