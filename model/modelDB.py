# config=utf-8
from model.DBUtil import db


class StudentUser(db.Model):
    username = db.Column(db.String(20), unique=False, primary_key=True)
    student_id = db.Column(db.String(13), unique=True)
    application_id = db.Column(db.Integer(), unique=True)

    __tablename__ = 'student_user'  # 指定对应数据库表student_user

    def __init__(self, username, student_id, application_id=None):
        """初始化StudentUser"""
        self.username = username
        self.student_id = student_id
        self.application_id = application_id

    def __repr__(self):
        return '<User %r>' % self.username

    def to_json(self):
        """将实例对象转化为json"""
        item = self.__dict__
        if "_sa_instance_state" in item:
            del item["_sa_instance_state"]
        return item

class StudentCourse(db.Model):
    cId=db.Column(db.Integer(), unique=True, primary_key=True)
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
    ID=db.Column(db.VARCHAR(18))

    def __init__(self, openID,name,studentID,institute,major,downGrade,choiceAfterGraduating,doctor,ID):
        """初始化application"""
        self.openID=openID
        self.name=name
        self.studentID=studentID
        self.institute=institute
        self.major=major
        self.downGrade=downGrade
        self.choiceAfterGraduating=choiceAfterGraduating
        self.doctor=doctor
        self.ID=ID
    def __repr__(self):
        return '<openID %r>' % self.openID
    def to_json(self):
        """将实例对象转化为json"""
        item = self.__dict__
        if "_sa_instance_state" in item:
            del item["_sa_instance_state"]
        return item