# config=utf-8
from model.DBUtil import db


class StudentUser(db.Model):
    username = db.Column(db.String(20), unique=False,primary_key = True)
    student_id=db.Column(db.String(13),unique=True)
    application_id=db.Column(db.Integer(),unique=True)

    __tablename__ = 'student_user'#指定对应数据库表student_user

    def __init__(self,username,student_id,application_id=None):
        '''初始化StudentUser'''
        self.username=username
        self.student_id=student_id
        self.application_id=application_id

    def __repr__(self):
        return '<User %r>' % (self.username)

    def to_json(self):
        """将实例对象转化为json"""
        item = self.__dict__
        if "_sa_instance_state" in item:
            del item["_sa_instance_state"]
        return item





