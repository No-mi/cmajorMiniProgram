from flask import Blueprint

teacher = Blueprint("teacher", __name__)    # 实例化一个蓝图(Blueprint)对象

@teacher.route('/')
def getT():
    return 'teacher'

