# -*- coding: UTF-8 -*-
# from model.modelDB import Application
from sqlalchemy import or_

from .modelDB import *
from .studentCourseDB import getPassedCoursesByStudenID, getCreditStatistic


def getApplicationByIdName(name, openID, studentId):
    """根据姓名/微信编号/学号查询申请表信息"""
    application = Application.query.filter_by(or_(studentId == studentId, name == name, openID == openID))
    # return list(map(lambda x:x.cId,application))
    return application


def getApplicationByOpenID(openID):
    """根据姓名/微信编号/学号查询申请表信息"""
    application = Application.query.filter_by(openID=openID).first()
    if application:
        application.courses = getPassedCoursesByStudenID(application.studentID)
        application.otherFiles = getOtherFilesByStudentId(application.studentID)
        application.specialities = getSpecialties(application.studentID)
        return application
    return application


def insertApplicqtion(openID, studentName, studentID, institute, major, grade, downGrade, choiceAfterGraduating, doctor,
                      ID,
                      CET, CETScore, GPA, phoneNumber, academicRecord, CETRecord):
    """插入一个申请表信息"""
    application = Application(openID, studentName, studentID, institute, major, grade, downGrade, choiceAfterGraduating,
                              doctor, ID,
                              CET, CETScore, GPA, phoneNumber, academicRecord, CETRecord)
    db.session.add(application)
    db.session.commit()

def deleteApplication(name, openID, studentId):
    """根据姓名/微信编号/学号删除一个申请表信息"""
    Application.query.filter_by(or_(openID == openID, name=name, studentId=studentId)).delete()


def updateApplicationByOpenID(openID, studentName, studentID, institute, major, grade, downGrade, choiceAfterGraduating,
                              doctor, ID,
                              CET, CETScore, GPA, phoneNumber, academicRecord, CETRecord):
    """修改指定姓名用户的姓名"""
    Application.query.filter_by(openID=openID).update(
        {'name': studentName, 'studentID': studentID, 'phoneNumber': phoneNumber, 'institute': institute,
         'major': major, 'grade': grade,
         'downGrade': downGrade, 'choiceAfterGraduating': choiceAfterGraduating, 'doctor': doctor, 'ID': ID,
         'academicRecord': academicRecord,
         'CETRecord': CETRecord, 'CET': CET, 'CETScore': CETScore, 'GPA': GPA})

def getAllApplication():
    """获取所有申请信息"""
    applications = Application.query.all()
    for application in applications:
        application.courses = getPassedCoursesByStudenID(application.studentID)
        application.otherFiles = getOtherFilesByStudentId(application.studentID)
        application.specialities = getSpecialties(application.studentID)
    print("len", len(applications))
    return applications


def getPassedCoursesByStudenID(studentID):
    res = StudentCourse.query.filter_by(studentId=studentID, havePassed=1)
    courses = list(map(lambda x: x.cId, res))
    print("getCourse", courses)
    return courses


def getOtherFilesByStudentId(studentId):
    res = OtherFile.query.filter_by(studentID=studentId)
    otherFile = list(map(lambda x: x.path, res))
    return otherFile


def ApplicationTransfor(application):
    if (application):
        resJson = application.to_json()
        return resJson
    return application


def getSpecialties(studentID):
    res = Speciality.query.filter_by(studentID=studentID)
    specialities = list(map(lambda x: x.path, res))
    return specialities


def getSexStatistic():
    res = list(Application.query.all())
    resC = list(map(lambda x: int(x.ID[16:17]) % 2, res))
    return {"male": resC.count(1), "female": resC.count(0)}


def getGradeStatistic():
    result = list(db.session.execute('SELECT grade,COUNT(*) as num from application GROUP BY grade'))
    return list(map(lambda x: ({str(x.grade): x.num}), result))

def getMajorStatistic():
    result = list(db.session.execute('SELECT major,COUNT(*) as num from application GROUP BY major'))
    return list(map(lambda x: ({str(x.major): x.num}), result))

def getTotalStudent():
    return len(Application.query.all())

def setOtherFiles(otherFiles, studentID):
    for file in otherFiles:
        print('insert', file)
        otherfile = OtherFile(studentID, file)
        db.session.add(otherfile)
        db.session.commit()


def updateOtherFile(otherFiles, studentID):
    OtherFile.query.filter_by()


def setSpecialities(specialities, studentID):
    for file in specialities:
        print('insert', file)
        specialityFile = Speciality(studentID, file)
        db.session.add(specialityFile)
        db.session.commit()


def getSpecialStudentStatistic():
    return list(db.session.execute('select count(*) as count from application where speciality=0'))[0].count


def deleteOtherFile(studentID):
    OtherFile.query.filter_by(studentID=studentID).delete()


def deleteSpecialities(studentId):
    Speciality.query.filter_by(studentID=studentId).delete()

def getStatisticData():
    data = {'totalNum': getTotalStudent(), 'sex': getSexStatistic(), 'grade': getGradeStatistic(),
            'major': getMajorStatistic(), 'specialStudent': getSpecialStudentStatistic(),
            'credit': getCreditStatistic()}
    return data
