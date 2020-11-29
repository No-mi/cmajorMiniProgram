# from model.modelDB import Application
from sqlalchemy import or_
from .modelDB import *

def getApplicationByIdName(name, openID, studentId):
    """根据姓名/微信编号/学号查询申请表信息"""
    application = Application.query.filter_by(or_(studentId == studentId, name == name, openID == openID))
    # return list(map(lambda x:x.cId,application))
    return application


def getApplicationByOpenID(openID):
    """根据姓名/微信编号/学号查询申请表信息"""
    application = Application.query.filter_by(openID=openID).first()
    # return list(map(lambda x:x.cId,application))
    return application

def insertApplicqtion(openID, name, studentID, institute, major, grade, downGrade, choiceAfterGraduating, doctor, ID,
                      courses):
    """插入一个申请表信息"""
    application = Application(openID=openID, name=name, studentID=studentID, institute=institute,
                              major=major, grade=grade, downGrade=downGrade,
                              choiceAfterGraduating=choiceAfterGraduating, doctor=doctor, ID=ID)
    db.session.add(application)
    # TODO 插入申请时添加课程修读信息
    # for i in courses:
    #     course=
    db.session.commit()

def deleteApplication(name,openID,studentId):
    """根据姓名/微信编号/学号删除一个申请表信息"""
    Application.query.filter_by(or_(openID == openID, name=name, studentId=studentId)).delete()


def updateApplicationByOpenID(openID, name, studentID, institute, major, grade, downGrade, choiceAfterGraduating,
                              doctor, ID,
                              courses):
    """修改指定姓名用户的姓名"""
    Application.query.filter_by(openID=openID).update(
        {'name': name, 'studentID': studentID, 'institute': institute, 'major': major, 'grade': grade,
         'downGrade': downGrade,
         'choiceAfterGraduating': choiceAfterGraduating, 'doctor': doctor, 'ID': ID})


def getAllApplication():
    """获取所有申请信息"""
    applications = Application.query.all()
    print("len", len(applications))
    return applications


# TODO 获取性别统计信息
def getSexCount():
    pass


def getGradeStatistic():
    result = list(db.session.execute('SELECT grade,COUNT(*) from application GROUP BY grade'))
    print("结果", result)
    print("数据类型", type(result[0]))
    # map(lambda x:)
    return result
