# from model.modelDB import Application
# from sqlalchemy import or_
from .modelDB import *
from flask import flash

def getStudentCourseByCid(cID):
    """根据课程号查询StudentCourse信息"""
    studentCourse = StudentCourse.query.filter_by(cID=cID)
    # return list(map(lambda x:x.cId,application))
    return studentCourse

def getStudentCourseByStudentId(studentId):
    """根据学号查询StudentCourse信息"""
    studentCourse = StudentCourse.query.filter_by(studentId=studentId)
    # return list(map(lambda x:x.cId,application))
    return studentCourse

def insertStudentCourse(cId,havePassed,studentId):
    """插入一个StudentCourse信息"""
    studentCourse = StudentCourse(cId=cId,havePassed=havePassed,studentId=studentId)
    db.session.add(studentCourse)
    db.session.commit()

def deleteStudentCourse(studentId):
    """根据学号删除一个StudentCourse信息"""
    studentCourse=StudentCourse.query.filter_by(studentId=studentId)
    try:
        db.session.delete(studentCourse)
        db.session.commit()
    except Exception as e:
        print(e)
        flash('删除失败')
        db.session.rollback()


def updateStudentCourse(cID,havePassed,studentId):
    """修改指定学号用户的cID和havePassed"""
    StudentCourse.query.filter_by(studentId=studentId).update({'cID': cID,'havePassed':havePassed})
