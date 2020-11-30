import json

from flask import Blueprint

from model.applicationDB import getAllApplication, getGradeStatistic, getSexCount, getMajorStatistic
from model.studentCourseDB import getPassedCoursesByStudenID, getCreditStatistic

admin = Blueprint("admin", __name__)  # 实例化teacher蓝图


@admin.route('/getAllApplication')
def getApplications():
    applications = getAllApplication()
    return json.dumps(list(map(lambda x: x.to_json(), applications)))


@admin.route('/getSexInfo')
def getSexInfo():
    res = getSexCount()
    return {"male": res.count(1), "female": res.count(0)}


@admin.route('/getGradeInfo')
def getGradeInfo():
    res = getGradeStatistic()
    return json.dumps(list(res))


@admin.route('/getMajorInfo')
def getMajorInfo():
    res = getMajorStatistic()
    return json.dumps(list(res))


# TODO 获取课程修读数据
@admin.route('/getCousesInfo')
def getCourseInfo():
    pass


@admin.route('/getCredit', methods=['GET'])
def getCredit():
    return json.dumps(getCreditStatistic())
