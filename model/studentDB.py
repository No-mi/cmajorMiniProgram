from .modelDB import *


def getStudentUserByUserName(username):
    """根据姓名查询学生信息"""
    user = StudentUser.query.filter_by(username=username).first()
    print(user)
    return user


def getStudentUserByStudentID(student_id):
    """根据学号查找学生信息"""
    user = StudentUser.query.filter_by(student_id=student_id).first()
    print(user)
    return user


def insertStudent(username, student_id):
    """插入一个学生用户"""
    user = StudentUser(username=username, student_id=student_id)
    db.session.add(user)
    db.session.commit()


def deleteStudent(student_id):
    """删除一个学生用户"""
    StudentUser.query.filter_by(student_id=student_id).delete()


def updateStudentInfo(student_id, username):
    """修改指定学号学生用户名"""
    StudentUser.query.filter_by(student_id=student_id).update({'username': username})
