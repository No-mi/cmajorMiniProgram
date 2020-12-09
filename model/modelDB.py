# -*- coding: UTF-8 -*-
from model.DBUtil import db


class StudentUser(db.Model):
    name = db.Column(db.VARCHAR(20), unique=False, primary_key=True)
    openID = db.Column(db.VARCHAR(40), unique=True)

    __tablename__ = 'user'  # 指定对应数据库表user

    def __init__(self, name, openID):
        """初始化StudentUser"""
        self.name = name
        self.openID = openID

    def __repr__(self):
        return '<User %r>' % self.name

    def to_json(self):
        """将实例对象转化为json"""
        item = self.__dict__
        if "_sa_instance_state" in item:
            del item["_sa_instance_state"]
        return item

class StudentCourse(db.Model):
    cId=db.Column(db.VARCHAR(9), unique=True, primary_key=True)
    havePassed = db.Column(db.Integer(), unique=True)
    studentId=db.Column(db.VARCHAR(40), unique=True, primary_key=True)
    __tablename__ = 'studentcourse'  # 指定对应数据库表student_user

    def __init__(self, cId,havePassed,studentId):
        """初始化StudentUser"""
        self.cId=cId
        self.havePassed=havePassed
        self.studentId=studentId


    def __repr__(self):
        return '<User %r>' % self.username

    def to_json(self):
        """将实例对象转化为json"""
        item = self.__dict__
        if "_sa_instance_state" in item:
            del item["_sa_instance_state"]
        return item

class Application(db.Model):
    __tablename__ = 'application'  # 指定对应数据库表application
    openID = db.Column(db.VARCHAR(40), primary_key=True)
    name = db.Column(db.VARCHAR(20))  # 姓名
    studentID = db.Column(db.VARCHAR(13))  # 学号
    phoneNumber = db.Column(db.VARCHAR(11))  # 电话号码
    institute = db.Column(db.VARCHAR(20))  # 原学院
    major = db.Column(db.VARCHAR(20))  # 原专业
    downGrade = db.Column(db.Integer)  # 是否同意降级 0：是 1：否
    grade = db.Column(db.VARCHAR(4))  # 年级
    choiceAfterGraduating = db.Column(db.Integer)  # 毕业后选择 0：国外深造 1：国内读研 2：就业 3：待定
    doctor = db.Column(db.Integer)  # 是否打算读博 1：是  0：否
    ID = db.Column(db.VARCHAR(18))  # 身份证号
    academicRecord = db.Column(db.VARCHAR(200))  # 成绩单图片地址
    CETRecord = db.Column(db.VARCHAR(200))  # 四六级成绩单图片地址
    CET = db.Column(db.Integer)  # 上传的成绩 0：四级 1：六级
    CETScore = db.Column(db.Integer)  # 四六级成绩
    GPA = db.Column(db.Float)  # 绩点
    courses = []  # 已修读课程列表
    otherFiles = []
    specialities = []

    def __init__(self, openID, name, studentID, institute, major, grade, downGrade, choiceAfterGraduating, doctor, ID,
                 CET, CETScore, GPA, phoneNumber, academicRecord, CETRecord, specialitylen):
        """初始化application"""
        self.openID = openID
        self.name = name
        self.studentID = studentID
        self.institute = institute
        self.phoneNumber = phoneNumber
        self.major = major
        self.grade = grade
        self.downGrade = downGrade
        self.choiceAfterGraduating = choiceAfterGraduating
        self.doctor = doctor
        self.ID = ID
        self.CET = CET
        self.CETScore = CETScore
        self.GPA = GPA
        self.academicRecord = academicRecord
        self.CETRecord = CETRecord
        self.specialities = specialitylen

    def __repr__(self):
        return '<openID %r>' % self.openID

    def to_json(self):
        """将实例对象转化为json"""
        item = self.__dict__
        if "_sa_instance_state" in item:
            del item["_sa_instance_state"]
        return item

class Course(db.Model):
    __tablename__ = 'courses'  # 指定对应数据库表studentcourse

    cId=db.Column(db.VARCHAR(9), unique=True, primary_key=True)
    cname = db.Column(db.VARCHAR(20), unique=True)
    cinstitute=db.Column(db.VARCHAR(20), unique=True, primary_key=True)
    credit=db.Column(db.Integer())
    time=db.Column(db.VARCHAR(10))

    def __init__(self, cId,cname,cinstitute,credit,time):
        """初始化StudentUser"""
        self.cId=cId
        self.cname=cname
        self.cinstitute=cinstitute
        self.credit=credit
        self.time=time

    def __repr__(self):
        return '<cname %r>' % self.cname

    def to_json(self):
        """将实例对象转化为json"""
        item = self.__dict__
        if "_sa_instance_state" in item:
            del item["_sa_instance_state"]
        return item

class OtherFile(db.Model):
    __tablename__ = 'otherfiles'  # 指定对应数据库表studentcourse

    studentID = db.Column(db.VARCHAR(13), primary_key=True)  # 学号
    path = db.Column(db.VARCHAR(255), primary_key=True)  # 成绩单图片地址

    def __init__(self, studentID, path):
        """初始化StudentUser"""
        self.studentID = studentID
        self.path = path

    def __repr__(self):
        return '<cname %r>' % self.path

    def to_json(self):
        """将实例对象转化为json"""
        item = self.__dict__
        if "_sa_instance_state" in item:
            del item["_sa_instance_state"]
        return item

class Speciality(db.Model):
    __tablename__ = 'specialities'  # 指定对应数据库表studentcourse

    studentID = db.Column(db.VARCHAR(13), primary_key=True)  # 学号
    path = db.Column(db.VARCHAR(255), primary_key=True)  # 图片地址

    def __init__(self, studentID, path):
        """初始化StudentUser"""
        self.studentID = studentID
        self.path = path

    def __repr__(self):
        return '<cname %r>' % self.path

    def to_json(self):
        """将实例对象转化为json"""
        item = self.__dict__
        if "_sa_instance_state" in item:
            del item["_sa_instance_state"]
        return item


class Institutions(db.Model):
    __tablename__ = 'institution'  # 指定对应数据库表studentcourse

    institutionName = db.Column(db.VARCHAR(40), primary_key=True)
    majorName = db.Column(db.VARCHAR(40), unique=True, primary_key=True)

    def __init__(self, institutionName, majorName):
        """初始化StudentUser"""
        self.institutionName = institutionName
        self.majorName = majorName

    def __repr__(self):
        return '<cname %r>' % self.cname

    def to_json(self):
        """将实例对象转化为json"""
        item = self.__dict__
        if "_sa_instance_state" in item:
            del item["_sa_instance_state"]
        return item
