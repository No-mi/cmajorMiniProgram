# config=utf-8
from model.DBUtil import db
from model.couresDB import getCoursesByStudentId


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
    openID=db.Column(db.VARCHAR(40),primary_key=True)
    name=db.Column(db.VARCHAR(20))
    studentID=db.Column(db.VARCHAR(13))
    institute=db.Column(db.VARCHAR(20))
    major=db.Column(db.VARCHAR(20))
    downGrade=db.Column(db.Integer)
    choiceAfterGraduating=db.Column(db.Integer)
    doctor=db.Column(db.Integer)
    ID = db.Column(db.VARCHAR(18))
    courses = []

    def __init__(self, openID,name,studentID,institute,major,downGrade,choiceAfterGraduating,doctor,ID):
        """初始化application"""
        self.openID=openID
        self.name=name
        self.studentID=studentID
        self.institute=institute
        self.major=major
        self.downGrade=downGrade
        self.choiceAfterGraduating=choiceAfterGraduating
        self.doctor = doctor
        self.ID = ID

    def __repr__(self):
        return '<openID %r>' % self.openID

    def to_json(self):
        """将实例对象转化为json"""
        item = self.__dict__
        if "_sa_instance_state" in item:
            del item["_sa_instance_state"]
        return item

    def getCourses(self):
        self.courses = getCoursesByStudentId(self.studentID)

class Course(db.Model):
    __tablename__ = 'studentcourse'  # 指定对应数据库表studentcourse

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