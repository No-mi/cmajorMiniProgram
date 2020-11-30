# from model.modelDB import Application
# from sqlalchemy import or_
from .couresDB import getAllCourses
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


def insertStudentCourse(cId, havePassed, studentId):
    """插入一个StudentCourse信息"""
    studentCourse = StudentCourse(cId=cId, havePassed=havePassed, studentId=studentId)
    db.session.add(studentCourse)
    db.session.commit()


def deleteStudentCourse(studentId):
    """根据学号删除一个StudentCourse信息"""
    studentCourse = StudentCourse.query.filter_by(studentId=studentId)
    try:
        db.session.delete(studentCourse)
        db.session.commit()
    except Exception as e:
        print(e)
        flash('删除失败')
        db.session.rollback()


def updateStudentCourse(cID, havePassed, studentId):
    """修改指定学号用户的cID和havePassed"""
    StudentCourse.query.filter_by(studentId=studentId).update({'cID': cID, 'havePassed': havePassed})


def setCourseByStudentID(courses, studentID):
    coursesAll = getAllCourses()
    print("setCourse调用", coursesAll)
    for course in coursesAll:
        if course in courses:
            print(studentID)
            studentCourse = StudentCourse(cId=course, havePassed=1, studentId=studentID)
            db.session.add(studentCourse)
            db.session.commit()
        else:
            studentCourse = StudentCourse(cId=course, havePassed=0, studentId=studentID)
            db.session.add(studentCourse)
            db.session.commit()


def getPassedCoursesByStudenID(studentID):
    res = StudentCourse.query.filter_by(studentId=studentID, havePassed=1)
    courses = list(map(lambda x: x.cId, res))
    print("getCourse", courses)
    return courses


def updateCourseByStudentID(courses, studentID):
    coursesAll = getAllCourses()
    print("courses", courses)
    for course in coursesAll:
        if course in courses:
            StudentCourse.query.filter_by(cId=course, studentId=studentID).update({'havePassed': 1})
        else:
            StudentCourse.query.filter_by(cId=course, studentId=studentID).update({'havePassed': 0})


def getCreditStatistic():
    result = list(db.session.execute(
        'SELECT t1.studentId,sum(t2.credit) as creditSum FROM studentcourse as t1 ,courses as t2 WHERE  t1.cId=t2.cId and t1.havePassed=1 GROUP BY t1.studentId'))
    totalCredit = int(list(db.session.execute('SELECT sum(credit) as totalCredit FROM courses'))[0].totalCredit)
    for i in result:
        print(i.studentId, i.creditSum, totalCredit)
    resP = list(map(lambda x: (int((int(x.creditSum) // (totalCredit * 0.7)))), result))
    print(resP)
    return {'pass': resP.count(1), "NotPass": resP.count(0)}
