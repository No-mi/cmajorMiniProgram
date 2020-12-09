# -*- coding: UTF-8 -*-
import json

from flask import Blueprint, request, session

from model.applicationDB import insertApplicqtion, updateApplicationByOpenID, getApplicationByOpenID, deleteOtherFile, \
    deleteSpecialities, setOtherFiles, setSpecialities, getSpecialties, getOtherFilesByStudentId, ApplicationTransfor, \
    getAllInstitutionInfo
# from model.couresDB import getCoursesByStudentId
from model.couresDB import getAllCourses
from model.studentCourseDB import setCourseByStudentID, getPassedCoursesByStudenID, \
    getCreditStatistic, delCourseByStudentID
from model.studentDB import getStudentUserByUserName, insertStudent, deleteStudent, updateStudentInfo
from model.modelDB import StudentUser
from server.studentServer import checkUser, onLogin, decrypt, getExcel, outputdir
from until.fileUtil import saveImg

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


# @student.route('/getPassedCourseByStudentID', methods=['GET'])
# def getCourse():
#     student_id = request.args['student_id']
#     # courses = getCoursesByStudentId(student_id)
#     return json.dumps(list(map(lambda x: x.cId, courses)))

@student.route('/setSession', methods=['GET'])
def setSession():
    session.permanent = True
    session['username'] = 'sess'
    return 'sessionTest'


@student.route('/checkSession', methods=['GET'])
def checkSession():
    return session.get('username')


# openID=ooo&studentName=courseTest&studentID2018141531004&institute=wangan&major=wangan&grade=2018&downGrade=1&choiceAfterGraduating=1&doctor=1&ID=341602200008087181&courses=["107032030","10711500"]

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
    # academicRecord = 'static/academicRecord/' + "academicRecord" + studentID + '.pdf'
    if (speciality is None):
        specialitylen = 0
    else:
        specialitylen = len(speciality)

    setCourseByStudentID(courses, studentID)

    setOtherFiles(otherFile, studentID)
    setSpecialities(speciality, studentID)

    insertApplicqtion(openID, studentName, studentID, institute, major, grade, downGrade, choiceAfterGraduating, doctor,
                      ID,
                      CET, CETScore, GPA, phoneNumber, academicRecord, CETRecord, specialitylen)
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

    # 设置图片名
    # academicRecord = {"path": 'static/imgs/' + "academicRecord" + studentID + '.png', "img": academicRecord}

    # saveImg(academicRecord)
    # academicRecord = academicRecord['path']
    # academicRecord = 'static/academicRecord/' + "academicRecord" + studentID + '.pdf'
    #
    # CETRecord = {"path": 'static/imgs/' + "CETRecord" + studentID + '.png', "img": CETRecord}
    # # saveImg(CETRecord)
    # CETRecord = CETRecord['path']
    # if otherFile is not  None:
    #     for i in range(len(otherFile)):
    #         file = {"path": 'static/imgs/' + "otherFile" + str(studentID) + '-' + str(i) + '.png', "img": otherFile[i]}
    #         # saveImg(file)
    #         otherFile[i] = 'static/imgs/' + "otherFile" + str(studentID) + '-' + str(i) + '.png'
    # if speciality is  not None:
    #     for i in range(len(speciality)):
    #         file = {"path": 'static/imgs/' + "speciality" + str(studentID) + '-' + str(i) + '.png',
    #                 "img": speciality[i]}
    #         # saveImg(file)
    #         speciality[i] = 'static/imgs/' + "speciality" + str(studentID) + '-' + str(i) + '.png'
    # if(!academicRecord)
    if (speciality is None):
        specialitylen = 0
    else:
        specialitylen = len(speciality)

    updateApplicationByOpenID(openID, studentName, studentID, institute, major, grade, downGrade, choiceAfterGraduating,
                              doctor, ID,
                              CET, CETScore, GPA, phoneNumber, academicRecord, CETRecord, specialitylen)
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


# @student.route('/getApplication', methods=['GET'])
# def getApplication():
#     openID = request.args.get("openID")
#     appli = getApplicationByOpenID(openID)
#     appli.courses = getPassedCoursesByStudenID(appli.studentID)
#     appli.otherFiles=getOtherFilesByStudentId(appli.studentID)
#     appli.specialities=getSpecialties(appli.studentID)
#     return appli.to_json()

# openID=099&studentName=courseTest&studentID=2018141518751&institute=网安&major=网安&grade=2018&downGrade=1&choiceAfterGraduating=1&grade=2018&doctor=1&ID=341602200008087191&courses=["107032030","107115000","105366020","105367010","888004010","900001010","314030020","912002010","201080030","201137050"]&CET=1&CETScore=450&GPA=3.7

@student.route('/setExcel')
def excel():
    outputdir()
    return "OK"
