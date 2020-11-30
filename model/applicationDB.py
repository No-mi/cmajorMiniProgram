# -*- coding: UTF-8 -*-
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
    application.courses = getPassedCoursesByStudenID(application.studentID)  # 获取修读课程列表
    return application


def insertApplicqtion(openID, name, studentID,phoneNumber , institute, major, grade, downGrade, choiceAfterGraduating, doctor, ID,
                      academicRecord ,CETRecord ,otherFIle ,speciality ,courses, CET, CETScore, GPA):
    """插入一个申请表信息"""
    application = Application(openID=openID, name=name, studentID=studentID, phoneNumber=phoneNumber,institute=institute,
                              major=major, grade=grade, downGrade=downGrade,choiceAfterGraduating=choiceAfterGraduating,
                              doctor=doctor, ID=ID, academicRecord=academicRecord,CETRecord=CETRecord,otherFIle=otherFIle,speciality=speciality,
                              courses=courses,CET=CET, CETScore=CETScore, GPA=GPA)
    db.session.add(application)
    db.session.commit()

def deleteApplication(name, openID, studentId):
    """根据姓名/微信编号/学号删除一个申请表信息"""
    Application.query.filter_by(or_(openID == openID, name=name, studentId=studentId)).delete()


def updateApplicationByOpenID(openID, name, studentID, institute, major, grade, downGrade, choiceAfterGraduating,
                              doctor, ID,academicRecord,CETRecord,otherFIle,courses, CET, CETScore, GPA, phoneNumber):
    """修改指定姓名用户的姓名"""
    Application.query.filter_by(openID=openID).update(
        {'name': name, 'studentID': studentID, 'phoneNumber': phoneNumber, 'institute': institute, 'major': major, 'grade': grade,
         'downGrade': downGrade,'choiceAfterGraduating': choiceAfterGraduating, 'doctor': doctor, 'ID': ID, 'academicRecord':academicRecord,
         'CETRecord':CETRecord,'otherFIle':otherFIle,'courses':courses,'CET': CET, 'CETScore': CETScore, 'GPA': GPA})


def getAllApplication():
    """获取所有申请信息"""
    applications = Application.query.all()
    for application in applications:
        application.courses = getPassedCoursesByStudenID(application.studentID)
    print("len", len(applications))
    return applications


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


def getSpecialStudentStatistic():
    return list(db.session.execute('select count(*) as count from application where speciality=0'))[0].count


def getStatisticData():
    data = {'totalNum': getTotalStudent(), 'sex': getSexStatistic(), 'grade': getGradeStatistic(),
            'major': getMajorStatistic(), 'specialStudent': getSpecialStudentStatistic(),
            'credit': getCreditStatistic()}
    return data
