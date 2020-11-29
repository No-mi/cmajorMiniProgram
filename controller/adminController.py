import json

from flask import Blueprint

from model.applicationDB import getAllApplication, getGradeStatistic

admin = Blueprint("admin", __name__)  # 实例化teacher蓝图


@admin.route('/getAllApplication')
def getApplications():
    applications = getAllApplication()
    return json.dumps(list(map(lambda x: x.to_json(), applications)))


@admin.route('/getSexInfo')
def getSexInfo():
    return 0


@admin.route('/getGradeInfo')
def getGradeInfo():
    res = getGradeStatistic()
    return ")K"
