import json

from flask import Blueprint

from model.applicationDB import getAllApplication, getGradeStatistic, getMajorStatistic, getSexStatistic, \
    getStatisticData
from model.studentCourseDB import getPassedCoursesByStudenID, getCreditStatistic

admin = Blueprint("admin", __name__)  # 实例化teacher蓝图


@admin.route('/getAllApplication')
def getApplications():
    applications = getAllApplication()
    return json.dumps(list(map(lambda x: x.to_json(), applications)))


@admin.route('/getStatisticData')
def statisticData():
    return getStatisticData()
#
# @admin.route('/getSexInfo')
# def getSexInfo():
#     return getSexStatistic()
#
#
# @admin.route('/getGradeInfo')
# def getGradeInfo():
#     res = getGradeStatistic()
#     return json.dumps(list(res))
#
#
# @admin.route('/getMajorInfo')
# def getMajorInfo():
#     res = getMajorStatistic()
#     return json.dumps(list(res))
#
#
#
#
#
# @admin.route('/getCredit', methods=['GET'])
# def getCredit():
#     return json.dumps(getCreditStatistic())
