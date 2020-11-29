# from model.modelDB import Application
from sqlalchemy import or_
from .modelDB import *

def getApplicationByIdName(name,openID,studentId):
    """根据姓名/微信编号/学号查询申请表信息"""
    application = Application.query.filter_by(or_(studentId==studentId , name==name ,openID==openID))
    # return list(map(lambda x:x.cId,application))
    return application

def insertApplicqtion(openID, name, studentID, institute, major, downGrade, choiceAfterGraduating, doctor, ID, courses):
    """插入一个申请表信息"""
    application = Application(openID=openID, name=name, studentID=studentID, institute=institute,
                              major=major, downGrade=downGrade,
                              choiceAfterGraduating=choiceAfterGraduating, doctor=doctor, ID=ID)
    db.session.add(application)
    # TODO 插入申请时添加课程修读信息
    # for i in courses:
    #     course=
    db.session.commit()

def deleteApplication(name,openID,studentId):
    """根据姓名/微信编号/学号删除一个申请表信息"""
    Application.query.filter_by(or_(openID==openID,name=name,studentId=studentId)).delete()

def updateApplication(name,studentId):
    """修改指定姓名用户的姓名"""
    Application.query.filter_by(studentId=studentId).update({'name': name,})
