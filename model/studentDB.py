# -*- coding: UTF-8 -*-
from .modelDB import *


def getStudentUserByUserName(username):
    """根据姓名查询学生信息"""
    user = StudentUser.query.filter_by(name=username).first()
    print(user)
    return user

def getStudentUserByOpenID(openId):
    """根据微信用户id查找学生信息"""
    user = StudentUser.query.filter_by(openID=openId).first()
    return user

def insertStudent(username, student_id):
    """插入一个学生用户"""
    user = StudentUser(name=username, openID=student_id)
    db.session.add(user)
    db.session.commit()


def deleteStudent(student_id):
    """删除一个学生用户"""
    StudentUser.query.filter_by(openID=student_id).delete()


def updateStudentInfo(student_id, username):
    """修改指定微信编号学生用户名"""
    StudentUser.query.filter_by(openID=student_id).update({'name': username})
