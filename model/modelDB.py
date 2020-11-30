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
    downGrade = db.Column(db.Integer)  # 是否同意降级 0：不同意 1：同一
    grade = db.Column(db.VARCHAR(4))  # 年级
    choiceAfterGraduating = db.Column(db.Integer)  # 毕业后选择
    doctor = db.Column(db.Integer)  # 是否打算读博
    ID = db.Column(db.VARCHAR(18))  # 身份证号
    academicRecord = db.Column(db.VARCHAR(40))  # 成绩单图片地址
    CETRecord = db.Column(db.VARCHAR(100))  # 四六级成绩单图片地址
    otherFIle = db.Column(db.VARCHAR(100))  # 其他证明材料地址，若无则为0
    speciality = db.Column(db.VARCHAR(100))  # 不满足申报条件但是有特长的证明材料图片地址，若无则为0
    CET = db.Column(db.Integer)  # 上传的成绩 0：四级 1：六级
    CETScore = db.Column(db.Integer)  # 四六级成绩
    GPA = db.Column(db.Float)  # 绩点
    courses = []  # 已修读课程列表

    def __init__(self, openID, name, studentID, institute, major, grade, downGrade, choiceAfterGraduating, doctor, ID,
                 CET, CETScore, GPA, phoneNumber):
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
        # self.courses=getPassedCoursesByStudenID(self.studentID)

    def __repr__(self):
        return '<openID %r>' % self.openID

    def to_json(self):
        """将实例对象转化为json"""
        item = self.__dict__
        if "_sa_instance_state" in item:
            del item["_sa_instance_state"]
        return item

    # def getCourses(self):
    #     self.courses = getCoursesByStudentId(self.studentID)

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