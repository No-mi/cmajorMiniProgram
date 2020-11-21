from flask import Blueprint

teacher = Blueprint("teacher", __name__)    # 实例化teacher蓝图

@teacher.route('/')
def getT():
    return 'teacher'

