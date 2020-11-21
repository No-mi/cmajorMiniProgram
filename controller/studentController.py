from flask import Blueprint

student = Blueprint("student", __name__)    # 实例化student蓝图

@student.route('/')
def getstu():
    return 'stu'