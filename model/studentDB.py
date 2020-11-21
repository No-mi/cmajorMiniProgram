from .modelDB import *

def getStudentUserByUserName(username):
    """根据姓名查询学生信息"""
    user=StudentUser.query.filter_by(username=username).first()
    print(user)
    return user

def getStudentUserByStudentID(student_id):
    """根据学号查找学生信息"""
    user=StudentUser.query.filter_by(student_id=student_id).first()
    print(user)
    return user

def InsertStudent(username,student_id):
    """插入一个学生用户"""
    user=StudentUser(username=username,student_id=student_id)
    db.session.add(user)
    db.session.commit()