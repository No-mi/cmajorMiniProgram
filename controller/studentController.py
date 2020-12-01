# -*- coding: UTF-8 -*-

from flask import Blueprint, request, session

from model.applicationDB import insertApplicqtion, updateApplicationByOpenID, getApplicationByOpenID, deleteOtherFile, \
    deleteSpecialities, setOtherFiles, setSpecialities
# from model.couresDB import getCoursesByStudentId
from model.studentCourseDB import setCourseByStudentID, getPassedCoursesByStudenID, updateCourseByStudentID, \
    getCreditStatistic
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
    # print("student", studentName)
    openID = req.get("openID")
    studentID = req.get("studentID")
    institute = req.get("institute")
    major = req.get("major")
    grade = req.get("grade")
    downGrade = int(req.get("downGrade"))
    # print("dwonGrade", downGrade)
    choiceAfterGraduating = int(req.get("choiceAfterGraduating"))
    doctor = int(req.get("doctor"))
    ID = int(req.get("ID"))
    courses = req.get("courses")
    CET = req.get("CET")
    CETScore = req.get("CETScore")
    GPA = req.get("GPA")

    speciality = req.get('speciality')
    CETRecord = req.get('CETRecord')
    otherFile = req.get('otherFile')
    academicRecord = req.get('academicRecord')

    # 设置图片名
    academicRecord = {"path": 'static/imgs/' + "academicRecord" + studentID + '.png', "img": academicRecord}

    saveImg(academicRecord)
    academicRecord = academicRecord['path']

    CETRecord = {"path": 'static/imgs/' + "CETRecord" + studentID + '.png', "img": CETRecord}
    saveImg(CETRecord)
    CETRecord = CETRecord['path']

    for i in range(len(otherFile)):
        file = {"path": 'static/imgs/' + "otherFile" + str(studentID) + '-' + str(i) + '.png', "img": otherFile[i]}
        saveImg(file)
        otherFile[i] = 'static/imgs/' + "otherFile" + str(studentID) + '-' + str(i) + '.png'

    for i in range(len(speciality)):
        file = {"path": 'static/imgs/' + "speciality" + str(studentID) + '-' + str(i) + '.png', "img": speciality[i]}
        saveImg(file)
        speciality[i] = 'static/imgs/' + "speciality" + str(studentID) + '-' + str(i) + '.png'

    setCourseByStudentID(courses, studentID)

    setOtherFiles(otherFile, studentID)
    setSpecialities(speciality, studentID)

    insertApplicqtion(openID, studentName, studentID, institute, major, grade, downGrade, choiceAfterGraduating, doctor,
                      ID, courses, CET, CETScore, GPA, academicRecord, CETRecord)
    return "OK"


@student.route('/updateApplication', methods=['POST'])
def updateApplication():
    req = json.loads(request.get_data(as_text=True))
    print('req', req)

    studentName = req.get("name")
    # print("student", studentName)
    openID = req.get("openID")
    studentID = req.get("studentID")
    institute = req.get("institute")
    major = req.get("major")
    grade = req.get("grade")
    downGrade = int(req.get("downGrade"))
    # print("dwonGrade", downGrade)
    choiceAfterGraduating = int(req.get("choiceAfterGraduating"))
    doctor = int(req.get("doctor"))
    ID = int(req.get("ID"))
    courses = req.get("courses")
    CET = req.get("CET")
    CETScore = req.get("CETScore")
    GPA = req.get("GPA")

    speciality = req.get('speciality')
    CETRecord = req.get('CETRecord')
    otherFile = req.get('otherFile')
    academicRecord = req.get('academicRecord')

    # 设置图片名
    academicRecord = {"path": 'static/imgs/' + "academicRecord" + studentID + '.png', "img": academicRecord}

    saveImg(academicRecord)
    academicRecord = academicRecord['path']

    CETRecord = {"path": 'static/imgs/' + "CETRecord" + studentID + '.png', "img": CETRecord}
    saveImg(CETRecord)
    CETRecord = CETRecord['path']

    for i in range(len(otherFile)):
        file = {"path": 'static/imgs/' + "otherFile" + str(studentID) + '-' + str(i) + '.png', "img": otherFile[i]}
        saveImg(file)
        otherFile[i] = 'static/imgs/' + "otherFile" + str(studentID) + '-' + str(i) + '.png'

    for i in range(len(speciality)):
        file = {"path": 'static/imgs/' + "speciality" + str(studentID) + '-' + str(i) + '.png', "img": speciality[i]}
        saveImg(file)
        speciality[i] = 'static/imgs/' + "speciality" + str(studentID) + '-' + str(i) + '.png'

    # setCourseByStudentID(courses, studentID)
    #
    # setOtherFiles(otherFile,studentID)
    # setSpecialities(speciality,studentID)
    #
    #
    #
    # insertApplicqtion(openID, studentName, studentID, institute, major, grade, downGrade, choiceAfterGraduating, doctor,
    #                   ID, courses, CET, CETScore, GPA,academicRecord,CETRecord)
    #
    updateApplicationByOpenID(openID, studentName, studentID, institute, major, grade, downGrade, choiceAfterGraduating,
                              doctor,
                              ID, courses, CET, CETScore, GPA, academicRecord, CETRecord)
    updateCourseByStudentID(courses, studentID)

    deleteOtherFile(studentID)
    deleteSpecialities(studentID)
    setOtherFiles(otherFile, studentID)
    setSpecialities(speciality, studentID)

    return getApplicationByOpenID(openID).to_json()

@student.route('/getApplicationByOpenID', methods=['GET'])
def getAppli():
    openID = request.args.get("openID")
    return getApplicationByOpenID(openID).to_json()

@student.route('/login', methods=['GET'])
def login():
    code = request.args['code']


@student.route('/getApplication', methods=['GET'])
def getApplication():
    openID = request.args.get("openID")
    appli = getApplicationByOpenID(openID)
    appli.courses = getPassedCoursesByStudenID(appli.studentId)
    return appli.to_json()

# openID=099&studentName=courseTest&studentID=2018141518751&institute=网安&major=网安&grade=2018&downGrade=1&choiceAfterGraduating=1&grade=2018&doctor=1&ID=341602200008087191&courses=["107032030","107115000","105366020","105367010","888004010","900001010","314030020","912002010","201080030","201137050"]&CET=1&CETScore=450&GPA=3.7
